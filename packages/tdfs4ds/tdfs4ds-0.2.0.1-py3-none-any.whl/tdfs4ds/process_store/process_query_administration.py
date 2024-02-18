import teradataml as tdml
import tdfs4ds
from tdfs4ds.utils.query_management import execute_query_wrapper

def list_processes():
    """
    Retrieves and returns a list of all processes from the feature store.
    The function fetches details like process ID, type, view name, entity ID,
    feature names, feature version, and metadata.

    Returns:
    DataFrame: A DataFrame containing the details of all processes in the feature store.
    """

    # Constructing the SQL query to fetch process details
    query = f"""
    CURRENT VALIDTIME
    SELECT 
        PROCESS_ID ,
        PROCESS_TYPE ,
        VIEW_NAME ,
        ENTITY_ID ,
        FEATURE_NAMES ,
        FEATURE_VERSION AS PROCESS_VERSION,
        DATA_DOMAIN,
        METADATA
    FROM {tdfs4ds.SCHEMA}.{tdfs4ds.PROCESS_CATALOG_NAME}
    """

    # Optionally printing the query if configured to do so
    if tdml.display.print_sqlmr_query:
        print(query)

    # Executing the query and returning the result as a DataFrame
    try:
        return tdml.DataFrame.from_query(query)
    except Exception as e:
        print(str(e))
        print(query)




@execute_query_wrapper
def remove_process(process_id):
    """
    Deletes a process from the feature store's process catalog based on the given process ID.

    Args:
    process_id (str): The unique identifier of the process to be removed.

    Returns:
    str: SQL query string that deletes the specified process from the process catalog.
    """

    # Constructing SQL query to delete a process by its ID
    query = f"DELETE FROM {tdfs4ds.SCHEMA}.{tdfs4ds.PROCESS_CATALOG_NAME} WHERE process_id = '{process_id}'"

    # Returning the SQL query string
    return query

def get_process_id(view_name):
    