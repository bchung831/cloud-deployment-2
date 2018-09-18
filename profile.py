# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec
request = pc.makeRequestRSpec()
 
# Creates number of nodes specified by the user and also sets node-1 to have a public ID address
for i in range(4):
    node = request.XenVM("node-" + str(i))  

# Sets each node to run CentOS7-64-STD
for i in range(4):
    node.disk_image = "urn:publicide:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

# Sets each node to have their respected local IP address
for i in range(4):
    node+str(i).addAddress(rspec.IPv4Address("192.168.1."+str(i), "255.255.255.0"))

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec()
