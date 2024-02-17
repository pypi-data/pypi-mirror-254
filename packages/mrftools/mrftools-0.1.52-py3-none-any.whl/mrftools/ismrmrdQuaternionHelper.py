import math
import numpy as np
def ismrmrd_sign_of_directions(read_dir, phase_dir, slice_dir):
    r11 = read_dir[0]; r12 = phase_dir[0]; r13 = slice_dir[0]
    r21 = read_dir[1]; r22 = phase_dir[1]; r23 = slice_dir[1]
    r31 = read_dir[2]; r32 = phase_dir[2]; r33 = slice_dir[2]

    # Determinant should be 1 or -1
    deti = (r11 * r22 * r33) + (r12 * r23 * r31) + (r21 * r32 * r13) - (r13 * r22 * r31) - (r12 * r21 * r33) - (r11 * r23 * r32)
    
    if (deti < 0):
        return -1
    else:
        return 1

def ismrmrd_directions_to_quaternion(read_dir, phase_dir, slice_dir):
    r11 = read_dir[0]; r12 = phase_dir[0]; r13 = slice_dir[0]
    r21 = read_dir[1]; r22 = phase_dir[1]; r23 = slice_dir[1]
    r31 = read_dir[2]; r32 = phase_dir[2]; r33 = slice_dir[2]
    
    a = 1; b = 0; c = 0; d = 0; s = 0
    trace = 0
    xd=0; yd=0; zd=0
    quat = [0,0,0,0]

    # verify the sign of the rotation
    if (ismrmrd_sign_of_directions(read_dir, phase_dir, slice_dir) < 0):
        # flip 3rd column
        r13 = -r13
        r23 = -r23
        r33 = -r33
    
    # Compute quaternion parameters
    #  http://www.cs.princeton.edu/~gewang/projects/darth/stuff/quat_faq.html#Q55
    trace = 1.0 + r11 + r22 + r33
    if (trace > 0.00001): # simplest case
        s = math.sqrt(trace) * 2
        a = (r32 - r23) / s
        b = (r13 - r31) / s
        c = (r21 - r12) / s
        d = 0.25 * s
    else:
        # trickier case...
        # determine which major diagonal element has
        # the greatest value...
        xd = 1.0 + r11 - (r22 + r33); # 4**b**b
        yd = 1.0 + r22 - (r11 + r33); # 4**c**c
        zd = 1.0 + r33 - (r11 + r22); # 4**d**d
        # if r11 is the greatest 
        if (xd > 1.0):
            s = 2.0 * math.sqrt(xd)
            a = 0.25 * s
            b = (r21 + r12) / s
            c = (r31 + r13) / s
            d = (r32 - r23) / s
        
        # else if r22 is the greatest
        elif (yd > 1.0):
            s = 2.0 * math.sqrt(yd)
            a = (r21 + r12) / s
            b = 0.25 * s
            c = (r32 + r23) / s
            d = (r13 - r31) / s
        
        # else, r33 must be the greatest
        else:
            s = 2.0 * math.sqrt(zd)
            a = (r13 + r31) / s
            b = (r23 + r32) / s
            c = 0.25 * s
            d = (r21 - r12) / s

        if (a < 0.0):
            b = -b
            c = -c
            d = -d
            a = -a
    
    quat[0] = float(a)
    quat[1] = float(b)
    quat[2] = float(c)
    quat[3] = float(d)
    return quat

# http://www.cs.princeton.edu/~gewang/projects/darth/stuff/quat_faq.html#Q54 
def ismrmrd_quaternion_to_directions(quat):
    a = quat[0]; b = quat[1]; c = quat[2]; d = quat[3]
    read_dir=[0,0,0]; phase_dir=[0,0,0]; slice_dir=[0,0,0]

    read_dir[0] = 1.0 - 2.0 * (b * b + c * c)
    phase_dir[0] = 2.0 * (a * b - c * d)
    slice_dir[0] = 2.0 * (a * c + b * d)
    
    read_dir[1] = 2.0 * (a * b + c * d)
    phase_dir[1] = 1.0 - 2.0 * (a * a + c * c)
    slice_dir[1] = 2.0 * (b * c - a * d)
    
    read_dir[2] = 2.0 * (a * c - b * d)
    phase_dir[2] = 2.0 * (b * c + a * d)
    slice_dir[2] = 1.0 - 2.0 * (a * a + b * b)

    return (read_dir, phase_dir, slice_dir)

def GetAcquisitionSpaceOffsetsMM(acqHeader):
    quaternion = ismrmrd_directions_to_quaternion(acqHeader.read_dir, acqHeader.phase_dir, acqHeader.slice_dir);
    mm_offset_acquisition_space = np.array([0,0,0])
    mm_offset_acquisition_space[0] = (acqHeader.position[0] * acqHeader.read_dir[0]) + (acqHeader.position[1] * acqHeader.read_dir[1]) + (acqHeader.position[2] * acqHeader.read_dir[2]);
    mm_offset_acquisition_space[1] = (acqHeader.position[0] * acqHeader.phase_dir[0]) + (acqHeader.position[1] * acqHeader.phase_dir[1]) + (acqHeader.position[2] * acqHeader.phase_dir[2]);
    mm_offset_acquisition_space[2] = (acqHeader.position[0] * acqHeader.slice_dir[0]) + (acqHeader.position[1] * acqHeader.slice_dir[1]) + (acqHeader.position[2] * acqHeader.slice_dir[2]);
    return mm_offset_acquisition_space

def GetVoxelSize(FOV, MatrixSize, SliceThickness):
    voxel_size = np.array([0,0,0])
    voxel_size[0] = FOV[0]/MatrixSize[0]
    voxel_size[1] = FOV[1]/MatrixSize[1]
    voxel_size[2] = SliceThickness;
    return voxel_size

def GetAcquisitionSpaceOffsetVoxels(mm_offset_acquisition_space, voxel_size):
    voxel_offset_acquisition_space = np.array([0,0,0])
    voxel_offset_acquisition_space[0] = mm_offset_acquisition_space[0]/voxel_size[0];
    voxel_offset_acquisition_space[1] = mm_offset_acquisition_space[1]/voxel_size[1];
    voxel_offset_acquisition_space[2] = mm_offset_acquisition_space[2]/voxel_size[2];
