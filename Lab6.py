### A - Block A should be at the beginning of your code
import  ikpy
import  numpy  as  np
from  ikpy  import  plot_utils
import sim
import sys
import time
#### End of A

# Connecting CopelliaSim to python
sim.simxFinish(-1)
clientID = sim.simxStart('192.168.7.21', 19999, True, True, 10000, 5)
if clientID !=-1:
    print ("Connected to remote API server")
else:
    print ("Not connected to remote API server")
    sys.exit ("could not connect")

#Start paused simulation
err_code = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)

err_code,basejoint = sim.simxGetObjectHandle(clientID,"Base_Joint",sim.simx_opmode_blocking)

while True:
    print ("Hello World")
    pos_val=numpy.radians(0)
    err_code = sim.simxSetJointTargetVelocity(clientID,j1,pos_val,sim.simx_opmode_streaming)

    time.sleep(1)

    pos_val = numpy.radians(10)
    err_code = sim.simxSetJointTargetVelocity(clientID,j1,pos_val,sim.simx_opmode_streaming)

    time.sleep(1)

    pos_val = numpy.radians(30)
    err_code = sim.simxSetJointTargetVelocity(clientID,j1,pos_val,sim.simx_opmode_streaming)



### B Where do you think B block should go?
my_chain = ikpy.chain.Chain.from_urdf_file( "./resources/poppy_ergo.URDF" )

target_vector = [  0.1 , - 0.2 ,  0.1 ]
target_frame = np.eye( 4 )  # Homogeneous matrix [4x4] = [ 1 2 3]->(Rotation)[1x3]->position last row is  0 0 0 1
target_frame[: 3 ,  3 ] = target_vector
### End of B

### C Where do you think this part should go?
print ( "The angles of each joints are : " , my_chain.inverse_kinematics(target_frame))
the1, the2, the3, the4, the5, the6, the7 = my_chain.inverse_kinematics(target_frame)
### End of C

### D Where do you think C block should go?
# You need to add something similar to below:

# pos_val = the1 # For the first joint
# pos_val = the2 # for the second joint

### End of D
      