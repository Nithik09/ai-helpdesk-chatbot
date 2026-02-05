from app.database import SessionLocal
from app.models import User, Ticket, Document


def seed_if_empty():
    db = SessionLocal()
    try:
        if db.query(User).count() > 0:
            return

        users = [
            User(name="Alice Admin", role="admin"),
            User(name="Ivan IT", role="it_agent"),
            User(name="Eve Employee", role="employee"),
        ]

        tickets = [
            Ticket(title="VPN not connecting", status="OPEN", priority="MEDIUM", description="Cannot connect from home"),
            Ticket(title="Password reset", status="OPEN", priority="LOW", description="Forgot password"),
            Ticket(title="Laptop failure", status="IN_PROGRESS", priority="HIGH", description="Device not booting"),
        ]

        docs = [
            Document(title="VPN Troubleshooting", path="scripts/sample_docs/vpn_troubleshooting.md", allowed_roles="employee,it_agent,admin"),
            Document(title="Password Reset Policy", path="scripts/sample_docs/password_reset_policy.md", allowed_roles="employee,it_agent,admin"),
            Document(title="Onboarding Checklist", path="scripts/sample_docs/onboarding_checklist.md", allowed_roles="employee,it_agent,admin"),
            Document(title="Laptop Replacement Policy", path="scripts/sample_docs/laptop_replacement_policy.md", allowed_roles="employee,it_agent,admin"),
            Document(title="Incident Response Playbook", path="scripts/sample_docs/incident_response_playbook.md", allowed_roles="it_agent,admin"),
            Document(title="HR Admin Policy", path="scripts/sample_docs/hr_admin_policy.md", allowed_roles="admin"),
        ]

        db.add_all(users + tickets + docs)
        db.commit()
    finally:
        db.close()
