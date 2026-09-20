import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'lab'))
from safe_logger import event,to_json
class T(unittest.TestCase):
 def test_redaction(self):
  s=to_json(event('answer_saved',details={'email':'user@example.com','token':'abc','note':'call +7 999 123-45-67'}))
  self.assertNotIn('user@example.com',s); self.assertNotIn('+7 999',s); self.assertNotIn('abc',s)
 def test_metadata(self):
  e=event('validation_failed','warn',{'field':'name'}); self.assertIn('correlation_id',e); self.assertEqual(e['severity'],'warn')
if __name__=='__main__': unittest.main()
