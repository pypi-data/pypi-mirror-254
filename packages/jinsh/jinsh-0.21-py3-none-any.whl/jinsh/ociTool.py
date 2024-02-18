import oci
import sys
import os
DEFAULT_LOCATION = os.path.join('~', '.oci', 'config')
DEFAULT_PROFILE = "DEFAULT"

class vm:
    vmlist = {}
    def __init__(self,config_file=DEFAULT_LOCATION,profile=DEFAULT_PROFILE):
        self.config_file = config_file
        self.profile = profile
        self.config = oci.config.from_file(file_location=self.config_file, profile_name=self.profile)
        self.core_client = oci.core.ComputeClient(self.config)

    def listVM(self):
        response = self.core_client.list_instances(compartment_id=self.config["compartment_id"])
        #print(response.data)
        for item in response.data:
            name = item.display_name
            ocid = item.id
            self.vmlist[name] = ocid
    def action(self,name,action):
        if name in self.vmlist:
            self.actionOCI(self.vmlist[name],action)
        else:
            self.listVM()
            if name in self.vmlist:
                self.actionOCI(self.vmlist[name], action)
            else:
                print("Can't find the VM you input")
    def actionOCI(self,ocid,action):
        instance_action_response = self.core_client.instance_action(
            instance_id=ocid,
            action=action)


