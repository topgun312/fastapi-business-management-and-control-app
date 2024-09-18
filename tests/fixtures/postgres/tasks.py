from uuid import UUID

TASKS = (
  {
        'id': UUID('97fa13cb-d481-4772-b27d-954c1a217702'),
        'title': 'Sell a Ferrari SF90 Stradale',
        'description': 'Sell a Ferrari supercar in 24 hours',
        'author_id': UUID('0a11b269-d752-43e3-a836-1b7b8d8a78c3'),
        'responsible_id': UUID('e58196d8-82eb-4f18-8f64-9db0bdfaf3b7'),
        'observers': [UUID('0982d535-c313-4832-8855-8189f47ce06d')],
        'performers': [UUID('e58196d8-82eb-4f18-8f64-9db0bdfaf3b7')],
        'created_at': '2024-09-16T07:57:48.914473',
        'updated_at':  '2024-09-16T07:57:48.914473',
        'deadline': '2024-09-16 21:03:48',
        'status': 'TASK IN PROCESS',
        'time_estimate': 24,
  }
)
