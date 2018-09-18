# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context
pc = portal.Context()

# Describes the parameters // section 8.8
portal.context.defineParameter( "n", "Number of VMs", portal.ParametreType.Integer, 1)

# Retrieves the values the user inputs // section 8.8
usr = portal.context.bindParameters() 

# Create a Request object to start building the RSpec
request = pc.makeRequestRSpec()
 
# Presents and error to the user if the value is not within the boundary // section 8.8
if usr.n <1 or usr.n >4: 
    pc.reportError( portal.ParameterError("Value inputed must be between 1 and 4")
                   
link = request.LAN("lan")
                          
# Creates number of nodes specified by the user 
for i in range(usr.n):
    node = request.XenVM("node-" + str(i+1)) # Creates number of nodes
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    interface = node.addInterface("iface"+str(i+1))
    interface.component_id = "eth"
    interface.addAddress(rspec.IPv4Address("192.168.1."+str(i+1), "255.255.255.0")) # Sets each of the nodes to have their respected IP address
    link.addInterface(iface)             
    if (i+1) == 1
          node.routable_control_ip = "true" # sets node-1 to have a public ID
    
# Print the RSpec to the enclosing page.
pc.printRequestRSpec()
