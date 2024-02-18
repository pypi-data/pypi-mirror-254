def wait_for_instance_state(api_client, linode_id, required_state='running'):
    import time, linode_api4
    """
    Wait for Linode instance state

    :param api_client: the linode_api4.client object to connect with
    :param linode_id: the ID of the target linode instance
    :parm linode_name: the Label of the target linode instance
    :parm required_state: Default is running
    :return: THe current status of the instance
    """
    while True:
        try:
            linodes = api_client.linode.instances(linode_api4.Instance.id == linode_id)
        except linode_api4.errors.ApiError as e:
            print(f"Error during Linode API call: {e}")

        # Parse Data
        for current_linode in linodes:
            if current_linode.id == linode_id:
                linode_instance = current_linode

        # Print the current status
        current_status = linode_instance.status
        if current_status != required_state:
            print(f"Current Linode Status is '{current_status}'. Waiting for status of '{required_state}'", end='\r', flush=True)

        else:
            print(f"Linode is now {required_state}.")
            break

        # Wait for 1 second before the next iteration
        time.sleep(1)

    return current_status

if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="The linode api client to connect to linode with.",required=True, type=LinodeClient)
    parser.add_argument("--linode_id", help="The ID of the target instance",required=True, type=int)
    parser.add_argument("--required_state",required=False, type=str,default="running",
                        help="The ID of the target instance")
    args=parser.parse_args()
    wait_for_instance_state(api_client=args.api_client,
                            linode_id=args.linode_id,
                            required_state=args.required_state)