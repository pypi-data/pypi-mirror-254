def swap_ipv4_addresses(api_client, instance1, instance2):
    import linode_api4
    """
    Swap IPv4 address between linode instances

    :param api_client: A linode_api4.client object to use as connection to linode
    :param instance1: A linode_api4.instance object representing the first instance in the swap
    :param instance2: A linode_api4.instance object representing the second instance in the swap
    """
    try:
        ipv4_address1 = instance1.ipv4[0]
        ipv4_address2 = instance2.ipv4[0]

        result = api_client.networking.ips_assign(instance1.region,
            {
            "address": ipv4_address1,
            "linode_id": instance2.id
            },
            {
            "address": ipv4_address2,
            "linode_id": instance1.id
            }
        )
        print(f"IPv4 addresses swapped between Linode instances {instance1.id} and {instance2.id}.")
    except linode_api4.errors.ApiError as e:
        print(f"Error during Linode API call: {e}")
if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient, Instance

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="The linode api client to connect to linode with.",required=True, type=LinodeClient)
    parser.add_argument("--instance1", help="The first instance involved in the swap",required=True, type=Instance)
    parser.add_argument("--instance2", help="The second instance involved in the swap",required=True, type=Instance)
    
    args=parser.parse_args()
    swap_ipv4_addresses(api_client=args.api_client,
                        instance1=args.instance1,
                        instance2=args.instance2)