def rename_linode_instance(instance, new_name):
    import linode_api4
    """
    Rename a Linode instance.

    :param instance: A linode_api4.Instance object representing the Linode instance to rename.
    :param new_name: The new name for the Linode instance.
    :param api_client: The linode_api4.Api object to use for making API calls.
    :return: True if the renaming is successful, False otherwise.
    """
    try:
        # Perform the Linode instance rename
        instance.label = new_name
        instance.save()

        # Display success message
        print(f"Linode instance {instance.id} renamed to {new_name}")
        return True
    except linode_api4.ApiError as e:
        # Display error message
        print(f"Error renaming Linode instance: {e}")
        return False
    
if __name__ == "__main__":
    import argparse
    from linode_api4 import Instance

    parser=argparse.ArgumentParser()

    parser.add_argument("--instance", help="The linode instance to rename.",required=True, type=Instance)
    parser.add_argument("--new_name", help="The new name of the instance",required=True, type=str)
    
    args=parser.parse_args()
    rename_linode_instance(instance=args.instance,new_name=args.new_name)