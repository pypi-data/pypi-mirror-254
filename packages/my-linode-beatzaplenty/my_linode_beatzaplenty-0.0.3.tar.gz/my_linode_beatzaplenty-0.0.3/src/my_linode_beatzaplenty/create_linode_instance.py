def create_linode_instance(api_client, plan, region, image, linode_username, label, root_password, firewall, stackscript, booted):
    import linode_api4
    """
    Create a new Linode instance with the specified parameters.

    :param api_client: The linode_api4.Api object to use for making API calls.
    :param plan: The Linode plan ID specifying the resources for the new instance.
    :param region: The Linode region ID where the new instance will be created.
    :param image: The Linode image ID to use for the new instance.
    :param linode_username: Linode user that can access the instance. Assigns SSH Key
    :param label: The label for the new Linode instance.
    :param root_password: The root password for the new Linode instance.
    :param firewall: Optional firewall ID to assign to the new Linode instance.
    :param stackscript: Optional Stackscript ID to assign to the new Linode Instance
    :param booted: Optional Bool to keep instance powered off after provisioning
    :return: A linode_api4.Instance object representing the newly created Linode instance.
    """

    try:
        new_instance = api_client.linode.instance_create(plan,
                                                   region,
                                                   image,
                                                   None,
                                                   authorized_users=[linode_username],
                                                   label=label,
                                                   root_pass=root_password,
                                                   stackscript=stackscript,
                                                   firewall=firewall,
                                                   booted=booted)
        # Display success message
        print(f"Linode instance {new_instance.id} created successfully.")
        return new_instance
    except linode_api4.ApiError as e:
        # Display error message
        print(f"Error creating Linode instance: {e}")
        return None
    
if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", required=True, type=LinodeClient,
                        help="The linode api_client object to use for the connection")

    parser.add_argument("--plan",default="g6-nanode-1",required=False, type=str,
                        help="The linode plan ID to use to create the instance. Default is 'g6-nanode-1'")
    
    parser.add_argument("--region",default="ap-southeast",required=False, type=str,
                        help="The region to create the new instance in. Default is 'ap-southeast'")
    
    parser.add_argument("--image",default="linode/debian12",required=False, type=str,
                        help="The image to use for the new instnace. Default is 'linode/debian12'")
    
    parser.add_argument("--linode_username",required=True, type=str,
                        help="The Linode Username that can access the new instance. Assigns SSH Key to instance")
    
    parser.add_argument("--label",required=True, type=str,
                        help="The label for the new instance.")
    
    parser.add_argument("--root_password",required=True, type=str,
                        help="The root user password for the new instance.")
    
    parser.add_argument("--firewall",required=False, type=int,
                        help="An ID number for an existing firewall to be applied to the new instance")
    
    parser.add_argument("--stackscript",required=False, type=int,
                        help="An ID number for an existing stackscript to be applied to the new instance")
    
    parser.add_argument("--booted",required=False, type=bool, default=True,
                        help="Boot the instance once it has been created. Defaults to true")

    args=parser.parse_args()

    create_linode_instance(api_client=args.api_client, 
                           plan=args.plan, 
                           region=args.region, 
                           image=args.image, 
                           linode_username=args.linode_username, 
                           label=args.label, 
                           root_password=args.root_password, 
                           firewall=args.firewall, 
                           stackscript=args.stackscript, 
                           booted=args.booted)