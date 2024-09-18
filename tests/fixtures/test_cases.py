from contextlib import nullcontext as does_not_raise

# url, company_name, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_CREATE_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/create_department/',
        'Supercars company',
        {
          'name': 'Sale department',
          'parent': 'Supercars company',
        }, {}, 201, {
            'name': 'Sale department',
            'id': 1,
            'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
            'head_user_id': None,
            'path': 'Supercars company.Sale department',
        }, does_not_raise(),
    ),
# not valid request body (incorrect company)

    (
         'api/structure/create_department/',
         'Adidas Company',
        {
           'name': 'Sale department',
           'parent': 'Adidas Company',
        }, {}, 422, {}, does_not_raise(),
    ),
]

# url, struct_adm_name, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/update_department/Sale department',
        'Sale department',
        {
          'name': 'New sale department',
        }, {}, 200, {
            'name': 'New sale department',
            'id': 1,
            'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
            'head_user_id': None,
            'path': 'Supercars company.New sale department',
        }, does_not_raise(),
    ),
# not valid request body (incorrect struct_adm_name)

    (
      'api/structure/update_department/Old sale department',
      'Old sale department',
        {
           'name': 'New sale department',
        }, {}, 422, {}, does_not_raise(),
    ),
]
# url, struct_adm_name, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/delete_department/Sale department',
        'Sale department',
         {}, 204, {}, does_not_raise(),
    ),
# not valid request body (incorrect struct_adm_name)

    (
      'api/structure/update_department/Old sale department',
      'Old sale department',
        {}, 422, {}, does_not_raise(),
    ),
]

# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_CREATE_POSITION_ROUTE = [
# positive case
    (
        'api/structure/create_position/',
        {
            'name': 'Repair department head',
            'description': 'Heads the repair department',
        }, {}, 201, {
            'name': 'Repair department head',
            'description': 'Heads the repair department',
            'id': 4,
        }, does_not_raise(),
    ),
# not valid request body (incorrect description)

    (
         'api/structure/create_position/',
        {
          'name': 'Repair department head',
          'description': 1234,
        }, {}, 422, {}, does_not_raise(),
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
        }, {}, 200, {
            'name': 'Repair department head and senior repairman',
            'description': 'Heads the repair department',
            'id': 4,
        }, does_not_raise(),
    ),
# not valid request body (incorrect name)

    (
         'api/structure/update_position/Repair department head',
         'Repair department head',
        {
          'name': 1234,
          'description': 'Heads the repair department',
        }, {}, 422, {}, does_not_raise(),
    ),
]

# url, position_name, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_POSITION_ROUTE = [
# positive case
    (
        'api/structure/delete_position/Repair department head',
        'Repair department head',
        {}, 204, {}, does_not_raise(),
    ),
# not valid request body (incorrect position)

    (
      'api/structure/delete_position/Repair head',
      'Repair head',
      {}, 422, {}, does_not_raise(),
    ),
]

# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_USERS_TO_POSITION_ROUTE = [
# positive case
    (
        'api/structure/add_users_to_position/',
        {
          'user_id': [
            '0982d535-c313-4832-8855-8189f47ce06d',
          ],
          'position_id': 3,
        }, {}, 201, [
          {
            'id': 'eed1178a-b3b2-41ed-8950-1b1da97bb9f9',
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
            'position_id': 3,
          },
        ], does_not_raise(),
    ),
# not valid request body (incorrect position_id)

    (
         'api/structure/add_users_to_position/',
        {
          'user_id': [
            '0982d535-c313-4832-8855-8189f47ce06d',
          ],
          'position_id': '3',
        }, {}, 422, {}, does_not_raise(),
    ),
]

# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_POSITION_TO_DEPARTMENT_ROUTE = [
# positive case
    (
        'api/structure/add_position_to_division/',
        {
          'struct_adm_id': 1,
          'position_id': 1,
        }, {}, 201, [

            {
          'struct_adm_id': 1,
          'position_id': 1,
          'id': '88bc79ef-5818-4866-9091-12bf678f2828',
            },

        ], does_not_raise(),
    ),
# not valid request body (incorrect position_id)
    (
      'api/structure/add_position_to_division/',
      {
        'struct_adm_id': 10,
        'position_id': 1,
      }, {}, 422, {}, does_not_raise(),
    ),
]

# url, user_id, struct_adm_name, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_DEPARTMENT_HEAD_ROUTE = [
# positive case
    (
        'api/structure/add_department_head/',
        '07cd5c88-214e-432b-8da0-9f840beca0aa',
        'Repair department',
          {}, 201, {
          'name': 'Repair department',
          'id': 2,
          'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
          'head_user_id': '07cd5c88-214e-432b-8da0-9f840beca0aa',
          'path': 'Supercars company.Repair department',
        }, does_not_raise(),
    ),
# not valid request body (incorrect struct_adm_name)
    (
      'api/structure/add_department_head/',
      '07cd5c88-214e-432b-8da0-9f840beca0aa',
      'Logistic department',
      {}, 422, {}, does_not_raise(),
    ),
]

# url, task_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_TASK_ROUTE = [
# positive case
    (
        'api/tasks/get_task/97fa13cb-d481-4772-b27d-954c1a217702',
        '97fa13cb-d481-4772-b27d-954c1a217702',
          {}, 200, {
            'title': 'Sell a Ferrari SF90 Stradale',
            'description': 'Sell a Ferrari supercar in 24 hours',
            'author_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'responsible_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              },
            ],
            'deadline': '2024-09-16 21:03:48',
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
            'id': '97fa13cb-d481-4772-b27d-954c1a217702',
          }, does_not_raise(),
    ),
# not valid request body (incorrect task_id)
    (
      'api/tasks/get_task/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      {}, 422, {}, does_not_raise(),
    ),
]

# url, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_ALL_TASKS_ROUTE = [
# positive case
    (
        'api/tasks/get_tasks/',

          {}, 200, [
          {
            'title': 'Sell a Ferrari SF90 Stradale',
            'description': 'Sell a Ferrari supercar in 24 hours',
            'author_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'responsible_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              },
            ],
            'deadline': '2024-09-16 21:03:48',
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
            'id': '97fa13cb-d481-4772-b27d-954c1a217702',
          },
          ], does_not_raise(),
    ),
]

# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_CREATE_TASK_ROUTE = [
# positive case
    (
        'api/tasks/create_task/',
          {
            'title': 'Sell a Ferrari SF90 Stradale',
            'description': 'Sell a Ferrari supercar in 24 hours',
            'author_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'responsible_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              },
            ],
            'deadline': '',
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
          },
          {}, 201, {
            'title': 'Sell a Ferrari SF90 Stradale',
            'description': 'Sell a Ferrari supercar in 24 hours',
            'author_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'responsible_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              },
            ],
            'deadline': '2024-09-16 21:03:48',
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
            'id': '97fa13cb-d481-4772-b27d-954c1a217702',
          }, does_not_raise(),
    ),
# not valid request body (incorrect task data)
    (
      'api/tasks/create_task/',
      {},
      {}, 422, {}, does_not_raise(),
    ),
]

# url, task_id, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_TASK_ROUTE = [
# positive case
    (
        'api/tasks/update_task/97fa13cb-d481-4772-b27d-954c1a217702',
        '97fa13cb-d481-4772-b27d-954c1a217702',
          {
            'title': 'Sell a Lamborghini Gallardo',
            'description': 'Sell a Lamborghini Gallardo supercar in 24 hours',
            'author_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'responsible_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              },
            ],
            'deadline': '',
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
          },
          {}, 200, {
            'title': 'Sell a Lamborghini Gallardo',
            'description': 'Sell a Lamborghini Gallardo supercar in 24 hours',
            'author_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'responsible_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'observers': [
              {
                'id': '0982d535-c313-4832-8855-8189f47ce06d',
              },
            ],
            'performers': [
              {
                'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              },
            ],
            'deadline': '2024-09-16 21:03:48',
            'status': 'TASK IN PROCESS',
            'time_estimate': 24,
            'id': '97fa13cb-d481-4772-b27d-954c1a217702',
          }, does_not_raise(),
    ),
# not valid request body (incorrect task_id)
    (
      'api/tasks/update_task/819700e7-575d-431c-9ef9-038a6ffeb644',
      '819700e7-575d-431c-9ef9-038a6ffeb644',
      {},
      {}, 422, {}, does_not_raise(),
    ),
]

# url, task_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_TASK_ROUTE = [
# positive case
    (
      'api/tasks/delete_task/97fa13cb-d481-4772-b27d-954c1a217702',
      '97fa13cb-d481-4772-b27d-954c1a217702',
        {}, 204, {}, does_not_raise(),
    ),
# not valid request body (incorrect position)

    (
      'api/tasks/delete_task/819700e7-575d-431c-9ef9-038a6ffeb644',
      '819700e7-575d-431c-9ef9-038a6ffeb644',
      {}, 422, {}, does_not_raise(),
    ),
]


# url, account_email, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_CHECK_ACCOUNT_ROUTE = [
# positive case
    (
      'api/company/reg/check_account/andrey@example.com',
      'andrey@example.com',
      {}, 200, {
        "status": 200,
        "detail": "A message with an invite_code has been sent to email andrey@example.com"
      }, does_not_raise(),
    ),
# not valid request body (email already exists)

    (
      'api/company/reg/check_account/petr@example.com',
      'petr@example.com',
      {}, 422, {}, does_not_raise(),
    ),
]

# url, account, invite_code, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_SIGN_UP_ROUTE = [
# positive case
    (
      'api/company/reg/sign_up',
      'andrey@example.com',
      5555,
      {}, 200, {
        "status": 200,
        "detail": f"The invite_code and email are valid! Please complete the registration of the company"
      }, does_not_raise(),
    ),
# not valid request body (email incorrect)

    (
      'api/company/reg/sign_up',
      'andrey333@example.com',
      5555,
      {}, 422, {}, does_not_raise(),
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
                'password': 'andrey111',
              },
              'account': {
                'email': 'andrey@example.com',
              },
              'company': {
                'name': 'Football products',
                'address': 'Moscow, Mira 44',
                'description': 'The company is engaged in the sale of goods for football',
                'website': 'www.moscowfootball.com',
              },
            },
        {}, 201, {
            'name': 'Football products',
            'address': 'Moscow, Mira 44',
            'description': 'The company is engaged in the sale of goods for football',
            'website': 'www.moscowfootball.com',
            'id': '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
            'created_at': '2024-09-14T12:17:16.128986',
            'updated_at': '2024-09-14T12:17:16.128986',
        }, does_not_raise(),
    ),
# not valid request body (incorrect data)
    (
      'api/company/reg/sign_up_complete',
      {}, {}, 422, {}, does_not_raise(),
    ),
]

# url, company_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_COMPANY_BY_ID_ROUTE = [
# positive case
    (
        'api/company/reg/get_company/8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
        '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
          {}, 200, {
             'name': 'Football products',
            'address': 'Moscow, Mira 44',
            'description': 'The company is engaged in the sale of goods for football',
            'website': 'www.moscowfootball.com',
            'id': '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
            'created_at': '2024-09-14T12:17:16.128986',
            'updated_at': '2024-09-14T12:17:16.128986',
          }, does_not_raise(),
    ),
# not valid request body (incorrect company_id)
    (
      'api/company/reg/get_company/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      {}, 422, {}, does_not_raise(),
    ),
]

# url, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_ALL_COMPANIES_ROUTE = [
# positive case
    (
        'api/company/reg/get_all_companies',
          {}, 200, [
          {
            'name': 'Supercars company',
            'address': 'Moscow, Lenina 23',
            'description': 'The company is engaged in the sale and rental of supercars',
            'website': 'www.moscowsc.com',
            'id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
            'created_at': '2024-09-14T12:17:16.128986',
            'updated_at': '2024-09-14T12:17:16.128986',
          },
          {
             'name': 'Football products',
            'address': 'Moscow, Mira 44',
            'description': 'The company is engaged in the sale of goods for football',
            'website': 'www.moscowfootball.com',
            'id': '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
            'created_at': '2024-09-14T12:17:16.128986',
            'updated_at': '2024-09-14T12:17:16.128986',
          },
          ], does_not_raise(),
    ),
]

# url, company_id, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_COMPANY_BY_ID_ROUTE = [
# positive case
    (
        'api/company/reg/update_company/8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
        '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
          {
            'name': 'Football products and souvenirs',
            'address': 'Moscow, Mira 44',
            'description': 'The company is engaged in the sale of goods for football',
            'website': 'www.moscowfootball.com',
                        },
          {}, 200, {
             'name': 'Football products and souvenirs',
            'address': 'Moscow, Mira 44',
            'description': 'The company is engaged in the sale of goods for football',
            'website': 'www.moscowfootball.com',
            'id': '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
            'created_at': '2024-09-14T12:17:16.128986',
            'updated_at': '2024-09-14T12:17:16.128986',
          }, does_not_raise(),
    ),
# not valid request body (incorrect company_id)
    (
      'api/company/reg/get_company/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      {
        'name': 'Football products and souvenirs',
        'address': 'Moscow, Mira 44',
        'description': 'The company is engaged in the sale of goods for football',
        'website': 'www.moscowfootball.com',
      },
      {}, 422, {}, does_not_raise(),
    ),
]

# url, company_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_DELETE_COMPANY_BY_ID_ROUTE = [
# positive case
    (
        'api/company/reg/delete_company/8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
        '8e7c67ac-a027-4dc4-a418-e469c3d9a7ce',
          {}, 204, {}, does_not_raise(),
    ),
# not valid request body (incorrect company_id)
    (
      'api/company/reg/get_company/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
        {}, 422, {}, does_not_raise(),
    ),
]

# url, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_MEMBER_TO_COMPANY_ROUTE = [
# positive case
    (
        'api/member/reg/add_member',
        {
          'user': {
            'first_name': 'Oleg',
            'last_name': 'Olegov',
          },
          'account': {
            'email': 'oleg@example.com',
          },
        },
        {}, 201, {
          'status': 201,
          'detail': 'User Oleg Olegov create. Confirm your profile in the email and complete the registration',
          }, does_not_raise(),
    ),
# not valid request body (incorrect email)
    (
      'api/member/reg/add_member',
      {
        'user': {
          'first_name': 'Oleg',
          'last_name': 'Olegov',
        },
        'account': {
          'email': 123,
        },
      },
      {}, 422, {}, does_not_raise(),
    ),
]

# url, invite_code, password, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_ADD_PASSWORD_AND_END_REGISTRATION_ROUTE = [
# positive case
    (
        'api/member/reg/add_password',
        1234,
        b'$2b$12$t4cQOcNEHPmAkRZeG/vDb.L0fKVvQofpufWXIuCYitPOYhFjIT4x2',
        {}, 201, {
          'first_name': 'Oleg',
          'last_name': 'Olegov',
          'id': '0982d535-c313-4832-8855-8189f47ce06d',
          'registered_at': '2024-09-16T07:57:48.914473',
          'updated_at': '2024-09-16T07:57:48.914473',
          'is_active': True,
          'is_admin': False,
          'account': {
            'email': 'oleg@example.com',
            'id': '958b4855-5953-44a5-ad82-27c6a034d772',
          },
          'member': {
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
            'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
            'id': '6e949c9b-549e-4c5a-a062-601ec80e2692',
          },
         }, does_not_raise(),
    ),
# not valid request body (incorrect invite)
    (
        'api/member/reg/add_password',
        9999,
        b'$2b$12$t4cQOcNEHPmAkRZeG/vDb.L0fKVvQofpufWXIuCYitPOYhFjIT4x2',
        {}, 422, {}, does_not_raise(),
    ),
]

# url, user_id, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_MEMBER_INFO_BY_USER_ID_ROUTE = [
# positive case
    (
        'api/member/reg/get_member_info/0982d535-c313-4832-8855-8189f47ce06d',
        '0982d535-c313-4832-8855-8189f47ce06d',
       {}, 200,
        {
          'first_name': 'Oleg',
          'last_name': 'Olegov',
          'id': '0982d535-c313-4832-8855-8189f47ce06d',
          'registered_at': '2024-09-16T07:57:48.914473',
          'updated_at': '2024-09-16T07:57:48.914473',
          'is_active': True,
          'is_admin': False,
          'account': {
            'email': 'oleg@example.com',
            'id': '958b4855-5953-44a5-ad82-27c6a034d772',
          },
          'member': {
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
            'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
            'id': '6e949c9b-549e-4c5a-a062-601ec80e2692',
          },
        }, does_not_raise(),
    ),
# not valid request body (incorrect user_id)
    (
      'api/company/reg/get_company/e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
      {}, 422, {}, does_not_raise(),
    ),
]

# url,  headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_GET_ALL_USERS_INFO_ROUTE = [
# positive case
    (
        'api/member/reg/get_all_users_info',
       {}, 200,
        [
          {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
            'registered_at': '2024-09-16T07:57:48.914473',
            'updated_at': '2024-09-16T07:57:48.914473',
            'is_active': True,
            'is_admin': True,
            'account': {
              'email': 'ivan@example.com',
              'id': '4311b77d-11bf-45ab-bbaf-a153ccab56bc',
            },
            'member': {
              'user_id': '0a11b269-d752-43e3-a836-1b7b8d8a78c3',
              'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
              'id': '55f45683-5d5a-4b16-88ba-ea5163a84429',
            },
          },
          {
            'first_name': 'Petr',
            'last_name': 'Petrov',
            'id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
            'registered_at': '2024-09-16T07:57:48.914473',
            'updated_at': '2024-09-16T07:57:48.914473',
            'is_active': True,
            'is_admin': False,
            'account': {
              'email': 'petr@example.com',
              'id': 'ea1112ab-32b0-4737-84e3-fd272d1613dd',
            },
            'member': {
              'user_id': 'e58196d8-82eb-4f18-8f64-9db0bdfaf3b7',
              'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
              'id': '8d6192eb-489f-44f7-9d63-86aebe8ef430',
            },
          },

          {
            'first_name': 'Oleg',
            'last_name': 'Olegov',
            'id': '0982d535-c313-4832-8855-8189f47ce06d',
            'registered_at': '2024-09-16T07:57:48.914473',
            'updated_at': '2024-09-16T07:57:48.914473',
            'is_active': True,
            'is_admin': False,
            'account': {
              'email': 'oleg@example.com',
              'id': '958b4855-5953-44a5-ad82-27c6a034d772',
            },
            'member': {
              'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
              'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
              'id': '6e949c9b-549e-4c5a-a062-601ec80e2692',
            },
          },
          {
            'first_name': 'Nikita',
            'last_name': 'Naumov',
            'id': '07cd5c88-214e-432b-8da0-9f840beca0aa',
            'registered_at': '2024-09-16T07:57:48.914473',
            'updated_at': '2024-09-16T07:57:48.914473',
            'is_active': True,
            'is_admin': False,
            'account': {
              'email': 'nikita@example.com',
              'id': '5cdd0e9c-4ea2-429b-b108-b39eea7f3b77',
            },
            'member': {
              'user_id': '07cd5c88-214e-432b-8da0-9f840beca0aa',
              'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
              'id': 'e6627a72-9d7f-48ae-80ea-b661d294c6c2',
            },
          },
          ],
          does_not_raise(),
    ),
]

# url, email, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_ACCOUNT_EMAIL_ROUTE = [
# positive case
    (
        'api/work_data/email_update',
        'oleg@example.com',
        {
            'email': 'newoleg@example.com',
        },

       {}, 200,
        {
          'email': 'newoleg@example.com',
          'id': '958b4855-5953-44a5-ad82-27c6a034d772',
          'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
        }, does_not_raise(),
    ),
# not valid request body (incorrect email)
    (
      'api/work_data/email_update',
        'oldoleg@example.com',
        {
            'email': 'newoleg@example.com',
        },
      {}, 422, {}, does_not_raise(),
    ),
]

# url, first_name, last_name, json, headers, expected_status_code, expected_payload, expectation
PARAMS_TEST_UPDATE_USER_FIRST_AND_LAST_NAME_ROUTE = [
# positive case
    (
        'api/work_data/user_update',
        'Oleg',
        'Olegov',
        {
            'first_name': 'Oleg',
            'last_name': 'Denisov',
        },
       {}, 200,
        {
          'first_name': 'Oleg',
          'last_name': 'Denisov',
          'id': '0982d535-c313-4832-8855-8189f47ce06d',
          'registered_at': '2024-09-16T07:57:48.914473',
          'updated_at': '2024-09-16T07:57:48.914473',
          'is_active': True,
          'is_admin': False,
          'account': {
            'email': 'oleg@example.com',
            'id': '958b4855-5953-44a5-ad82-27c6a034d772',
          },
          'member': {
            'user_id': '0982d535-c313-4832-8855-8189f47ce06d',
            'company_id': 'fa6ce865-fb2f-4d8a-b80f-fdbd121ff095',
            'id': '6e949c9b-549e-4c5a-a062-601ec80e2692',
          },
        }, does_not_raise(),
    ),
# not valid request body (incorrect first_name)
    (
      'api/work_data/user_update',
        'Denis',
        'Olegov',
        {
            'first_name': 'Oleg',
            'last_name': 'Denisov',
        },
      {}, 422, {}, does_not_raise(),
    ),
]
