from uuid import UUID

USERS = (
  {
    'first_name': 'Ivan',
    'last_name': 'Ivanov',
    'id': UUID('0a11b269-d752-43e3-a836-1b7b8d8a78c3'),
    'registered_at': '2024-09-16T07:57:48.914473',
    'updated_at': '2024-09-16T07:57:48.914473',
    'is_active': True,
    'is_admin': True,
    'account': {
      'email': 'ivan@example.com',
      'id': UUID('4311b77d-11bf-45ab-bbaf-a153ccab56bc'),
    },
    'member': {
      'user_id': UUID('0a11b269-d752-43e3-a836-1b7b8d8a78c3'),
      'company_id': UUID('fa6ce865-fb2f-4d8a-b80f-fdbd121ff095'),
      'id': UUID('55f45683-5d5a-4b16-88ba-ea5163a84429'),
    },
  },
  {
    'first_name': 'Petr',
    'last_name': 'Petrov',
    'id': UUID('e58196d8-82eb-4f18-8f64-9db0bdfaf3b7'),
    'registered_at': '2024-09-16T07:57:48.914473',
    'updated_at': '2024-09-16T07:57:48.914473',
    'is_active': True,
    'is_admin': False,
    'account': {
      'email': 'petr@example.com',
      'id': UUID('ea1112ab-32b0-4737-84e3-fd272d1613dd'),
    },
    'member': {
      'user_id': UUID('e58196d8-82eb-4f18-8f64-9db0bdfaf3b7'),
      'company_id': UUID('fa6ce865-fb2f-4d8a-b80f-fdbd121ff095'),
      'id': UUID('8d6192eb-489f-44f7-9d63-86aebe8ef430'),
    },
  },

  {
    'first_name': 'Oleg',
    'last_name': 'Olegov',
    'id': UUID('0982d535-c313-4832-8855-8189f47ce06d'),
    'registered_at': '2024-09-16T07:57:48.914473',
    'updated_at': '2024-09-16T07:57:48.914473',
    'is_active': True,
    'is_admin': False,
    'account': {
      'email': 'oleg@example.com',
      'id': UUID('958b4855-5953-44a5-ad82-27c6a034d772'),
    },
    'member': {
      'user_id': UUID('0982d535-c313-4832-8855-8189f47ce06d'),
      'company_id': UUID('fa6ce865-fb2f-4d8a-b80f-fdbd121ff095'),
      'id': UUID('6e949c9b-549e-4c5a-a062-601ec80e2692'),
    },
  },
  {
    'first_name': 'Nikita',
    'last_name': 'Naumov',
    'id': UUID('07cd5c88-214e-432b-8da0-9f840beca0aa'),
    'registered_at': '2024-09-16T07:57:48.914473',
    'updated_at': '2024-09-16T07:57:48.914473',
    'is_active': True,
    'is_admin': False,
    'account': {
      'email': 'nikita@example.com',
      'id': UUID('5cdd0e9c-4ea2-429b-b108-b39eea7f3b77'),
    },
    'member': {
      'user_id': UUID('07cd5c88-214e-432b-8da0-9f840beca0aa'),
      'company_id': UUID('fa6ce865-fb2f-4d8a-b80f-fdbd121ff095'),
      'id': UUID('e6627a72-9d7f-48ae-80ea-b661d294c6c2'),
    },
  },
)
