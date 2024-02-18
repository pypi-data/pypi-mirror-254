# Acclaim Badge XBlock

This Open edX XBlock allows students to claim an Acclaim badge when they meet
the minimum required grade to pass a course.

## Installing

This XBlock can be installed with `pip` as with any other Python package:

```bash
pip install .
```

## Configuring

In Studio you can set the following values when configuring the XBlock:

* **Display Name**: this is the title displayed to students int he course
* **Organization ID**: the ID of your organization on Acclaim
* **Badge template ID**: the ID of the badge template to be issued
* **Acclaim API key**: key for the Acclaim API
* **Sandbox mode?**: use the Sandbox environment for testing, make sure it is set to `False` before publishing the course

# Example configuration in `lms.env.json`

```
"XBLOCK_SETTINGS": {
    "AcclaimBadgeXBlock": {
        "Organiation 1": {
            "api_key": "secret",
            "id": "org_id"
        },
        "Organization 2": {
            "api_key": "secret",
            "id": "org2_id",
            "url": "https://sandbox.youracclaim.com/api/v1"
        }
    }
}
```

# Apache 2.0 License

Copyright 2020 IBM Skills Network

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.