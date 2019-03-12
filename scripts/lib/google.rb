require 'google/apis/sheets_v4'
require 'googleauth'
require 'googleauth/stores/file_token_store'

OOB_URI = 'urn:ietf:wg:oauth:2.0:oob'.freeze
CREDENTIALS_PATH = './config/secret_credentials.json'.freeze
TOKEN_PATH = './config/secret_token.yaml'.freeze
SCOPE = Google::Apis::SheetsV4::AUTH_SPREADSHEETS_READONLY

##
# Ensure valid credentials, either by restoring from the saved credentials
# files or intitiating an OAuth2 authorization. If authorization is required,
# the user's default browser will be launched to approve the request.
#
# @return [Google::Auth::UserRefreshCredentials] OAuth2 credentials
def authorize
  client_id = Google::Auth::ClientId.from_file(CREDENTIALS_PATH)
  token_store = Google::Auth::Stores::FileTokenStore.new(file: TOKEN_PATH)
  authorizer = Google::Auth::UserAuthorizer.new(client_id, SCOPE, token_store)
  user_id = 'default'
  credentials = authorizer.get_credentials(user_id)
  if credentials.nil?
    url = authorizer.get_authorization_url(base_url: OOB_URI)
    puts 'Open the following URL in the browser and enter the ' \
         "resulting code after authorization:\n" + url
    code = gets
    credentials = authorizer.get_and_store_credentials_from_code(
      user_id: user_id, code: code, base_url: OOB_URI
    )
  end
  credentials
end


# 4/CwFsdPX6uhQBFHGGSF__9rOaRfqLNMsDe4Cd6M3ESMVEmob2zq2MFN0