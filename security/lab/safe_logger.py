from __future__ import annotations
import json, re, uuid
from datetime import datetime, timezone
SENSITIVE={'password','token','authorization','cookie','email','phone','secret','api_key'}
EMAIL=re.compile(r'\b[^\s@]+@[^\s@]+\.[^\s@]+\b')
PHONE=re.compile(r'(?<!\d)(?:\+?7|8)?[\s()-]*\d{3}[\s()-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}(?!\d)')
def redact(value):
    if isinstance(value,dict): return {k:('[REDACTED]' if k.lower() in SENSITIVE else redact(v)) for k,v in value.items()}
    if isinstance(value,list): return [redact(v) for v in value]
    if isinstance(value,str): return PHONE.sub('[PHONE]', EMAIL.sub('[EMAIL]', value))[:240]
    return value
def event(event_type,severity='info',details=None,correlation_id=None):
    return {'ts':datetime.now(timezone.utc).isoformat(),'event_type':event_type,'severity':severity,'correlation_id':correlation_id or str(uuid.uuid4()),'details':redact(details or {})}
def to_json(evt): return json.dumps(evt, ensure_ascii=False, sort_keys=True)
