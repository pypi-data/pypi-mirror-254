def wait_for_completion(polling_thread):
    import time
    """
    Wait for Linode Event to complete

    :param polling_thread: A threading.thread object created from a linode_api4.polling object
    """
    print(f"waiting for completion")   
    polling_thread.start()
    start_time = time.time()
    while polling_thread.is_alive():
        elapsed_time_seconds = time.time() - start_time
        minutes, seconds = divmod(elapsed_time_seconds, 60)
        elapsed_time_formatted = f"{round(minutes)} minutes, {round(seconds)} seconds"
        print(f"Elapsed Time: {elapsed_time_formatted}", end="\r", flush=True)
    # Wait for the polling thread to finish
    print(f"Elapsed Time: {elapsed_time_formatted}", flush=True)
    polling_thread.join()
    print("Operation Complete")

if __name__ == "__main__":
    import argparse
    from linode_api4 import polling

    parser=argparse.ArgumentParser()

    parser.add_argument("--polling_thread", help="The linode polling_thread to watch for completion.",required=True, type=polling)
        
    args=parser.parse_args()
    wait_for_completion(polling_thread=args.polling_thread)