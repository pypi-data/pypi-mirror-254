def get_type_label(api_client, id):
    import linode_api4
    """
    Get Linode Plan label by ID

    :param api_client: A linode_api4.client object to use as the connection
    :param id: the ID of the plan to query for.
    :return: Returns the plan's label
    """
    try:
        all_types = api_client.linode.types()
        type_mapping = {type.id: type.label for type in all_types}
        return type_mapping.get(id, f"Label for type ID {id} not found")
    except linode_api4.errors.ApiError as e:
        print(f"Error during Linode API call: {e}")

if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="The linode api client to connect to linode with.",required=True, type=LinodeClient)
    parser.add_argument("--id", help="The firewall label to search on",required=True, type=str)
    
    args=parser.parse_args()
    get_type_label(api_client=args.api_client,id=args.id)