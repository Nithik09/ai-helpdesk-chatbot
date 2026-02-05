INSERT INTO users (name, role) VALUES
  ('Alice Admin', 'admin'),
  ('Ivan IT', 'it_agent'),
  ('Eve Employee', 'employee');

INSERT INTO documents (title, path, allowed_roles) VALUES
  ('VPN Troubleshooting Guide', 'data/docs/vpn_troubleshooting.md', 'employee,it_agent,admin'),
  ('Password Reset Policy', 'data/docs/password_reset_policy.md', 'employee,it_agent,admin'),
  ('Onboarding IT Checklist', 'data/docs/onboarding_it_checklist.md', 'employee,it_agent,admin'),
  ('Laptop Replacement Policy', 'data/docs/laptop_replacement_policy.md', 'employee,it_agent,admin'),
  ('Incident Response Playbook', 'data/docs/incident_response_playbook.md', 'it_agent,admin'),
  ('HR Compensation Policy (Restricted)', 'data/docs/hr_compensation_policy.md', 'admin');

INSERT INTO tickets (title, status, priority, description) VALUES
  ('VPN not connecting', 'OPEN', 'MEDIUM', 'User cannot connect to VPN from home'),
  ('Password reset request', 'OPEN', 'LOW', 'Forgot password, needs reset'),
  ('Laptop blue screen', 'IN_PROGRESS', 'HIGH', 'Device crashes during boot'),
  ('Email sync issue', 'OPEN', 'LOW', 'Outlook not syncing'),
  ('Multi-factor reset', 'RESOLVED', 'MEDIUM', 'MFA device replaced'),
  ('Software install request', 'OPEN', 'LOW', 'Need Tableau installed'),
  ('Wi-Fi drops', 'IN_PROGRESS', 'MEDIUM', 'Office Wi-Fi disconnects intermittently'),
  ('Printer offline', 'OPEN', 'LOW', 'Floor 3 printer not responding'),
  ('New hire setup', 'RESOLVED', 'MEDIUM', 'Provisioned laptop and accounts'),
  ('Security alert follow-up', 'OPEN', 'HIGH', 'Potential phishing report');
