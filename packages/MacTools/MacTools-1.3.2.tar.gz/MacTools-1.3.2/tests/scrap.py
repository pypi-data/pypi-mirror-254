# From OUI TESTS

# Fixed Test Data
MAL_RESPONSE_TEXT = 'HEADER\r\nMA-L,246D5E,"TEST Systems, Inc",1001 Someplace Road City AA 11111 US'
MAM_RESPONSE_TEXT = 'HEADER\r\nMA-M,79B74DA,TEST Labs,1001 Someplace Road City AA 11111 US'
MAS_RESPONSE_TEXT = 'HEADER\r\nMA-S,24B7BD603,Micro TEST Inc,1001 Someplace Road City AA 11111 US'

def determine_api_response(*args, **kwargs):
    mock_response = Mock()
    mock_response.status_code = 200
    response_map = {
        'MA-L': MAL_RESPONSE_TEXT,
        'MA-M': MAM_RESPONSE_TEXT,
        'MA-S': MAS_RESPONSE_TEXT,
        r'oui/oui.csv': MAL_RESPONSE_TEXT,
        r'oui28/mam.csv': MAM_RESPONSE_TEXT,
        r'oui36/oui36.csv': MAS_RESPONSE_TEXT,
        r'https://api.maclookup.app/v2/macs/': TEST_RECORD
    }
    for response_case, response in response_map.items():
        if isinstance(args[0], OUIType):
            mock_response.text = response_map.get(args[0].value)
            break
        if search(response_case, args[0]):
            mock_response.text = response
            break
    return mock_response

class TestOUICacheAPI(TestCase):
    """
    Test class to ensure API call and cache construction
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.patchers: list[_patch_default_new] = []
        cls.mock_response = Mock()
        cls.mock_response.status_code = 200

        oui_csv_patch = patch(f'{OUI_CORE_PATH}.get_oui_csv', side_effect=determine_api_response)
        # cls.patchers.append(oui_csv_patch)
        cls.patchers.append(patch('builtins.print', return_value=None))

        for patcher in cls.patchers:
            patcher.start()
    
    @classmethod
    def tearDownClass(cls) -> None:
        for patcher in cls.patchers:
            patcher.stop()