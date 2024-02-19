
def create_session(llm_api='openai', **kwargs):
    """Creates a new session.

    Args:
        llm_api (str, optional): _description_. Defaults to 'openai'.
    """


    params = {
        'api': llm_api,
    }
    params.update(kwargs)
    response = "Temp response"
    return response

def create_session_by_llms_only(llm_api='openai', **kwargs):
    """Creates a new session.

    Args:
        llm_api (str, optional): _description_. Defaults to 'openai'.
    """


    params = {
        'api': llm_api,
    }
    params.update(kwargs)
    response = "Temp response"
