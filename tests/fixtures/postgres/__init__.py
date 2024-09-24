from tests.fixtures.postgres.accounts import FAKE_ACCOUNTS
from tests.fixtures.postgres.companies import FAKE_COMPANIES
from tests.fixtures.postgres.invites import  FAKE_INVITES
from tests.fixtures.postgres.members import  FAKE_MEMBERS
from tests.fixtures.postgres.positions import FAKE_POSITIONS
from tests.fixtures.postgres.secrets import  FAKE_SECRETS
from tests.fixtures.postgres.struct_adm_positions import  FAKE_STRUCT_ADM_POSITIONS
from tests.fixtures.postgres.struct_adms import  FAKE_STRUCT_ADMS
from tests.fixtures.postgres.tasks import FAKE_TASKS, FAKE_OBSERVERS_TASKS, FAKE_PERFORMERS_TASKS
from tests.fixtures.postgres.user_positions import  FAKE_USER_POSITIONS
from tests.fixtures.postgres.users import FAKE_USERS

__all__ = (
  'FAKE_TASKS', 'FAKE_USERS', 'FAKE_SECRETS', 'FAKE_POSITIONS', 'FAKE_MEMBERS', 'FAKE_USER_POSITIONS', 'FAKE_STRUCT_ADM_POSITIONS',
  'FAKE_STRUCT_ADMS', 'FAKE_INVITES', 'FAKE_COMPANIES', 'FAKE_ACCOUNTS', 'FAKE_OBSERVERS_TASKS', 'FAKE_PERFORMERS_TASKS'
)
