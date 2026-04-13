
class ApiUrl:

    def api_url():
        return "https://api.restful-api.dev/objects"

    def put_patch_delete_url(self, object_id):
        return "https://api.restful-api.dev/objects/" + str(object_id)

    def collection_url():
        return "https://api.restful-api.dev/collections"

    def login_existing_user(self):
        return "https://api.restful-api.dev/login"

    def register_new_user(self):
        return "https://api.restful-api.dev/register"