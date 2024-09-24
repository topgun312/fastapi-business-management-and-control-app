from contextlib import nullcontext as does_not_raise


# url, company_name, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_CREATE_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/create_department/Aircraft_products',
        'Aircraft_products',
        {
          'name': 'New_sale_department',
          'parent': 'Aircraft_products',
        }, 201, {
            'name': 'New_sale_department',
            'company_id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
            'head_user_id': None,
            'path': 'Aircraft_products.New_sale_department',
        }, does_not_raise(),
    ),
# not valid request body (incorrect company)

    (
         'api/structure/create_department/',
         'Adidas_Company',
        {
           'name': 'Sale_department',
           'parent': 'Adidas_Company',
        }, 404, {}, does_not_raise(),
    ),
]

# url, struct_adm_name, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/update_department/Sale_department',
        'Sale_department',
        {
          'name': 'New_sale_department',
        }, 200, {
            'name': 'New_sale_department',
            'company_id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
            'head_user_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'path': 'Aircraft_products.New_sale_department',
        }, does_not_raise(),
    ),
# not valid request body (incorrect struct_adm_name)

    (
      'api/structure/update_department/Old_sale_department',
      'Old_sale_department',
        {
           'name': 'New_sale_department',
        }, 404, {}, does_not_raise(),
    ),
]
# url, struct_adm_name, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/delete_department/Sale_department',
        'Sale_department',
          204, does_not_raise(),
    ),
# not valid request body (incorrect struct_adm_name)

    (
      'api/structure/delete_department/Old_sale_department',
      'Old_sale_department',
        404, does_not_raise(),
    ),
]

# url, json,  expected_status_code, expected_payload, expectation
PARAMS_TEST_CREATE_POSITION_ROUTE = [
# positive case
    (
        'api/structure/create_position',
        {
            'name': 'New repair department head',
            'description': 'Heads the new repair department',
        },  201, {
            'name': 'New repair department head',
            'description': 'Heads the new repair department',
            'id': 1,
        }, does_not_raise(),
    ),
# not valid request body (incorrect description)

    (
         'api/structure/create_position',
        {
          'name': 'Repair department head',
          'description': 1234,
        }, 422, {
    'detail': [
       {          'input': 1234,
            'loc': [
                'body',
                'description',
            ],
            'msg': 'Input should be a valid string',
                  'type': 'string_type',
        }, ]
      }, does_not_raise(),
    ),
]

# url, position_name, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_POSITION_ROUTE = [
# positive case
    (
        'api/structure/update_position/Repair department head',
        'Repair department head',
        {
            'name': 'Repair department head and senior repairman',
            'description': 'Heads the repair department',
        }, 200, {
            'name': 'Repair department head and senior repairman',
            'description': 'Heads the repair department',
            'id': 4,
        }, does_not_raise(),
    ),
# not valid request body (incorrect name)

    (
         'api/structure/update_position/New Repair department head',
         'New Repair department head',
        {
          'name': '1234',
          'description': 'Heads the repair department',
        }, 404, {'detail': 'Position not found!',}, does_not_raise(),
    ),
]

# url, position_name, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_POSITION_ROUTE = [
# positive case
    (
        'api/structure/delete_position/Repair department head',
        'Repair department head',
        204, does_not_raise(),
    ),
# not valid request body (incorrect position)

    (
      'api/structure/delete_position/Repair head',
      'Repair head',
      404, does_not_raise(),
    ),
]

# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_USERS_TO_POSITION_ROUTE = [
# positive case
    (
        'api/structure/add_users_to_position',
        {
          'user_id': [
            '0982d535-c313-4832-8855-8189f47ce06d',
          ],
          'position_id': 3,
        }, 201, [
          {
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
            'position_id': 3,
          },
        ], does_not_raise(),
    ),
]

# url, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_POSITION_TO_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/add_position_to_division',
        {
          'struct_adm_id': 3,
          'position_id': 1,
        }, 201,
            {
          'struct_adm_id': 3,
          'position_id': 1,
            }, does_not_raise(),
    ),
# not valid request body (incorrect position_id)
    (
      'api/structure/add_position_to_division',
      {
        'struct_adm_id': 10,
        'position_id': 1,
      }, 404, {'detail': 'Department not found'}, does_not_raise(),
    ),
]

# url, user_id, struct_adm_name, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_DEPARTMENT_HEAD_ROUTE = [
# positive case
    (
        'api/structure/add_department_head/07cd5c88-214e-432b-8da0-9f840beca0aa/Repair_department',
        '07cd5c88-214e-432b-8da0-9f840beca0aa',
        'Repair_department',
          200, {
          'name': 'Repair_department',
          'id': 5,
          'company_id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
          'head_user_id': '07cd5c88-214e-432b-8da0-9f840beca0aa',
          'path': 'Aircraft_products.Repair_department',
        }, does_not_raise(),
    ),
# not valid request body (incorrect struct_adm_name)
    (
      'api/structure/add_department_head',
      '07cd5c88-214e-432b-8da0-9f840beca0aa',
      'Logistic_department',
      404, {'detail': 'Not Found'}, does_not_raise(),
    ),
]

# url, task_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_TASK_ROUTE = [
# positive case
    (
        'api/tasks/get_task/97fa13cb-d481-4772-b27d-954c1a217702',
        '97fa13cb-d481-4772-b27d-954c1a217702',
          200, {
            'title': 'Sell a Boing 777',
            'description': 'Sell a Boing 777',
            'author_id': 'fba99cad-8e39-4108-b692-ffe8ce3c5d70',
            'responsible_id': '7a937595-1206-4dae-8934-56cf4f46e71e',
            'observers': [
                            {
                            'id': '0982d535-c313-4832-8855-8189f47ce06d',
                            },
                         ],
            'performers': [
                            {
                            'id': '7a937595-1206-4dae-8934-56cf4f46e71e',
                            },
                         ],
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
            'id': '97fa13cb-d481-4772-b27d-954c1a217702',
          }, does_not_raise(),
    ),
# not valid request body (incorrect task_id)
    (
      'api/tasks/get_task/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      404, {}, does_not_raise(),
    ),
]

# url, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_ALL_TASKS_ROUTE = [
# positive case
    (
        'api/tasks/get_tasks',
          200, [
          {
            'title': 'Sell a Boing 777',
            'description': 'Sell a Boing 777',
            'author_id': 'fba99cad-8e39-4108-b692-ffe8ce3c5d70',
            'responsible_id': '7a937595-1206-4dae-8934-56cf4f46e71e',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': '7a937595-1206-4dae-8934-56cf4f46e71e',
              },
            ],
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
            'id': '97fa13cb-d481-4772-b27d-954c1a217702',
          },
          ], does_not_raise(),
    ),
]

# url, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_CREATE_TASK_ROUTE = [
# positive case
    (
        'api/tasks/create_task',
        {
          'title': 'Sell a Airbus 320',
          'description': 'Sell a Airbus 320',
          'author_id': '07cd5c88-214e-432b-8da0-9f840beca0aa',
          'responsible_id': '0982d535-c313-4832-8855-8189f47ce06d',
           'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': '7a937595-1206-4dae-8934-56cf4f46e71e',
              },
            ],
          'status': 'TASK IN PROCESS',
          'time_estimate': 24,
        },
          201,  {
          'title': 'Sell a Airbus 320',
          'description': 'Sell a Airbus 320',
          'author_id': '07cd5c88-214e-432b-8da0-9f840beca0aa',
          'responsible_id': '0982d535-c313-4832-8855-8189f47ce06d',
           'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': '7a937595-1206-4dae-8934-56cf4f46e71e',
              },
            ],
          'status': 'TASK IN PROCESS',
          'time_estimate': 24,
        }, does_not_raise(),
    ),
# not valid request body (incorrect task data)
    (
      'api/tasks/create_task',
      {},
      422, {}, does_not_raise(),
    ),
]

# url, task_id, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_TASK_ROUTE = [
# positive case
    (
        'api/tasks/update_task/97fa13cb-d481-4772-b27d-954c1a217702',
        '97fa13cb-d481-4772-b27d-954c1a217702',

          {
            'title': 'Sell a Boing 777-400',
            'description': 'Sell a Boing 777-400',
            'author_id': 'fba99cad-8e39-4108-b692-ffe8ce3c5d70',
            'responsible_id': '7a937595-1206-4dae-8934-56cf4f46e71e',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': '7a937595-1206-4dae-8934-56cf4f46e71e',
              },
            ],
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
          },

        200, {

            'title': 'Sell a Boing 777-400',
            'description': 'Sell a Boing 777-400',
            'author_id': 'fba99cad-8e39-4108-b692-ffe8ce3c5d70',
            'responsible_id': '7a937595-1206-4dae-8934-56cf4f46e71e',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': '7a937595-1206-4dae-8934-56cf4f46e71e',
              },
            ],
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
          },
           does_not_raise(),
    ),
# not valid request body (incorrect task_id)
    (
      'api/tasks/update_task/819700e7-575d-431c-9ef9-038a6ffeb644',
      '819700e7-575d-431c-9ef9-038a6ffeb644',
      {}, 422, {}, does_not_raise(),
    ),
]

# url, task_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_TASK_ROUTE = [
# positive case
    (
      'api/tasks/delete_task/97fa13cb-d481-4772-b27d-954c1a217702',
      '97fa13cb-d481-4772-b27d-954c1a217702',
         204, does_not_raise(),
    ),
# not valid request body (incorrect position)

    (
      'api/tasks/delete_task/819700e7-575d-431c-9ef9-038a6ffeb644',
      '819700e7-575d-431c-9ef9-038a6ffeb644',
      404, does_not_raise(),
    ),
]


# url, account_email, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_CHECK_ACCOUNT_ROUTE = [
# positive case
    (
      'api/company/reg/check_account/bob@example.com',
      'bob@example.com',
      {}, 200, {
        "status": 200,
        "detail": "A message with an invite_code has been sent to email bob@example.com"
      }, does_not_raise(),
    ),

# not valid request body (email already exists)

    (
      'api/company/reg/check_account/petr@example.com',
      'petr@example.com',
      {}, 409,  {"detail":"Such an email already exists"}, does_not_raise(),
    ),
]

#url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_SIGN_UP_ROUTE = [
# positive case
    (
      'api/company/reg/sign_up',
      {'account': 'ivan@example.com',
      'invite_code': 4433},
      {}, 200, {
        "status": 200,
        "detail": f"The invite_code and email are valid! Please complete the registration of the company"
      }, does_not_raise(),
    ),
# not valid request body (email incorrect)

    ('api/company/reg/sign_up',
      {'account': 'ivan333@example.com',
      'invite_code': 4433},
      {}, 404, {'detail': 'Account not found'} , does_not_raise(),
    ),
]



# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_SIGN_UP_COMPLETE_ROUTE = [
# positive case
    (
        'api/company/reg/sign_up_complete',
            {
              'user': {
                'first_name': 'Andrey',
                'last_name': 'Andreev',
              },
              'secret': {
                'password': 'andrey',
              },
              'account': {
                'email': 'andrey@example.com',
              },
              'company': {
                'name': 'Basketball_products',
                'address': 'Moscow, Gagarina, 3',
                'description': 'The company is engaged in the sale of goods for basketball',
                'website': 'www.moscowbasketball.com',
              },
            },
        {}, 201, {
            'name': 'Basketball_products',
            'address': 'Moscow, Gagarina, 3',
            'description': 'The company is engaged in the sale of goods for basketball',
            'website': 'www.moscowbasketball.com',
        }, does_not_raise(),
    ),
# not valid request body (incorrect data)
    (
      'api/company/reg/sign_up_complete',
      {
        'user': {
          'first_name': 'Andrey',
          'last_name': 'Andreev',
        },
        'secret': {
          'password': 'andrey',
        },
      }, {}, 422, {}, does_not_raise(),
    ),
]

# url, company_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_COMPANY_BY_ID_ROUTE = [
# positive case
    (
        'api/company/reg/get_company/07d3f795-0a6b-42af-866b-7cb517cd129a',
        '07d3f795-0a6b-42af-866b-7cb517cd129a',
        200,
        {
          'name': 'Aircraft_products',
          'address': 'Moscow, Gagarina 3',
          'description': 'The company is engaged in the sale and rental of aircraft',
          'website': 'www.moscowavia.com',
        }, does_not_raise(),
    ),
# not valid request body (incorrect company_id)
    (
      'api/company/reg/get_company/819700e7-575d-431c-9ef9-038a6ffeb644',
      '819700e7-575d-431c-9ef9-038a6ffeb644',
       404, {}, does_not_raise(),
    ),
]

# url, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_ALL_COMPANIES_ROUTE = [
# positive case
    (
        'api/company/reg/get_all_companies',
          {}, 200, [
          {
            'name': 'Supercars_company',
            'address': 'Moscow, Lenina 23',
            'description': 'The company is engaged in the sale and rental of supercars',
            'website': 'www.moscowsc.com',
          },
          {
             'name': 'Football_products',
            'address': 'Moscow, Mira 44',
            'description': 'The company is engaged in the sale of goods for football',
            'website': 'www.moscowfootball.com',
          },
          {
            'name': 'Aircraft_products',
            'address': 'Moscow, Gagarina 3',
            'description': 'The company is engaged in the sale and rental of aircraft',
            'website': 'www.moscowavia.com',
          },
          ], does_not_raise(),
    ),
]

# url, company_id, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_COMPANY_BY_ID_ROUTE = [
# positive case
    (
        'api/company/reg/update_company/07d3f795-0a6b-42af-866b-7cb517cd129a',
        '07d3f795-0a6b-42af-866b-7cb517cd129a',
          {
          'id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
          'name': 'Aircraft_and_helicopters_products',
          'address': 'Moscow, Gagarina 3',
          'description': 'The company is engaged in the sale and rental of aircraft and helicopters',
          'website': 'www.moscowavia.com',
                        },
            200, {
          'name': 'Aircraft_and_helicopters_products',
          'address': 'Moscow, Gagarina 3',
          'description': 'The company is engaged in the sale and rental of aircraft and helicopters',
          'website': 'www.moscowavia.com',
          }, does_not_raise(),
    ),
# not valid request body (incorrect company_id)
    (
      'api/company/reg/update_company/0982d535-c313-4832-8855-8189f47ce06d',
      '0982d535-c313-4832-8855-8189f47ce06d',
      {
        'id': '0982d535-c313-4832-8855-8189f47ce06d',
        'name': 'Aircraft_and_helicopters_products',
        'address': 'Moscow, Gagarina 3',
        'description': 'The company is engaged in the sale and rental of aircraft and helicopters',
        'website': 'www.moscowavia.com',
      },
      404, {}, does_not_raise(),
    ),
]

# url, company_id, headers, expected_status_code,  expectation
PARAMS_TEST_DELETE_COMPANY_BY_ID_ROUTE = [
# positive case
    (
        'api/company/reg/delete_company/07d3f795-0a6b-42af-866b-7cb517cd129a',
        '07d3f795-0a6b-42af-866b-7cb517cd129a',
         204, does_not_raise(),
    ),
# not valid request body (incorrect company_id)
    (
      'api/company/reg/delete_company/0982d535-c313-4832-8855-8189f47ce06d',
      '0982d535-c313-4832-8855-8189f47ce06d',
       404, does_not_raise(),
    ),
]

# url, json,  expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_MEMBER_TO_COMPANY_ROUTE = [
# positive case
    (
        'api/member/reg/add_member',
        {
          'user': {
            'first_name': 'Uriy',
            'last_name': 'Beglov',
          },
          'account': {
            'email': 'uriy@example.com',
          },
        },
        201, {
          'status': 201,
          'detail': 'User Uriy Beglov create. Confirm your profile in the email and complete the registration',
          }, does_not_raise(),
    ),
# not valid request body (incorrect email)
    (
      'api/member/reg/add_member',
      {
        'user': {
          'first_name': 'Uriy',
          'last_name': 'Beglov',
        },
        'account': {
          'email': 'oleg@example.com',
        },
      },
      400, {'detail': 'Such an email already exists'}, does_not_raise(),
    ),
]

# url, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_PASSWORD_AND_END_REGISTRATION_ROUTE = [
# positive case
    (
        'api/member/reg/add_password',
        {
          "invite_code": {
            "code": 9999
          },
          "password": {
            "password": "levyashin"
          }
        },
        201, {
          'first_name': 'Lev',
          'last_name': 'Yashin',
          'account': {
            'email': 'lev@example.com',
            'id': '060a0348-cafc-4f14-84ca-7172c9b84982',
            "user_id": "7a937595-1206-4dae-8934-56cf4f46e71e"
          },
          'member': {
            'user_id': '7a937595-1206-4dae-8934-56cf4f46e71e',
            'company_id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
            'id': '4d98bde4-b2d5-454c-8fee-e4fd9da627a4',
          },
         }, does_not_raise(),
    ),
# not valid request body (incorrect user_id)
  (
  'api/member/reg/add_password',
  {
    "invite_code": {
      "code": 1133
    },
    "password": {
      "password": "levyashin"
    }
  },
  404, {}, does_not_raise(),
  ),
]

# url, user_id, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_MEMBER_INFO_BY_USER_ID_ROUTE = [
# positive case
        (
          'api/member/reg/get_member_info/0982d535-c313-4832-8855-8189f47ce06d',
          '0982d535-c313-4832-8855-8189f47ce06d',
          200,
          {
            'first_name': 'Oleg',
            'last_name': 'Olegov',
            'account': {
              'email': 'oleg@example.com',
              'id': '958b4855-5953-44a5-ad82-27c6a034d772',
              "user_id": "0982d535-c313-4832-8855-8189f47ce06d"
            },
            'member': {
              'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
              'company_id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
              'id': '6e949c9b-549e-4c5a-a062-601ec80e2692',
            },
          }, does_not_raise(),
        ),
# not valid request body (incorrect user_id)
    (
      'api/company/reg/get_member_info/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      404, {}, does_not_raise(),
    ),
]


# url, email, json, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_ACCOUNT_EMAIL_ROUTE = [
# positive case
    (
        'api/work_data/email_update/oleg@example.com',
        'oleg@example.com',
        {
            'email': 'newoleg@example.com',
        },

       200,
        {
          'email': 'newoleg@example.com',
          'id': '958b4855-5953-44a5-ad82-27c6a034d772',
          'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
        }, does_not_raise(),
    ),
# not valid request body (incorrect email)
    (
      'api/work_data/email_update/oldoleg@example.com',
        'oldoleg@example.com',
        {
            'email': 'newoleg@example.com',
        },
      404, {}, does_not_raise(),
    ),
]

# url, first_name, last_name, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_USER_FIRST_AND_LAST_NAME_ROUTE = [
# positive case
    (
        'api/work_data/user_update/Oleg/Olegov',
        'Oleg',
        'Olegov',
        {
            'first_name': 'Oleg',
            'last_name': 'Denisov',
        },
       200,
        {
          'first_name': 'Oleg',
          'last_name': 'Denisov',
          'account': {
            'email': 'oleg@example.com',
            'id': '958b4855-5953-44a5-ad82-27c6a034d772',
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d'
          },
          'member': {
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
            'company_id': '07d3f795-0a6b-42af-866b-7cb517cd129a',
            'id': '6e949c9b-549e-4c5a-a062-601ec80e2692',
          },
        }, does_not_raise(),
    ),
# not valid request body (incorrect first_name)
    (
      'api/work_data/user_update/Denis/Olegov',
        'Denis',
        'Olegov',
        {
            'first_name': 'Oleg',
            'last_name': 'Denisov',
        },
      404, {}, does_not_raise(),
    ),
]
