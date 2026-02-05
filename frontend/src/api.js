const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function fetchUsers() {
  const res = await fetch(`${API_URL}/users`);
  return res.json();
}

export async function sendChat(payload) {
  const res = await fetch(`${API_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  return res.json();
}

export async function fetchLogs() {
  const res = await fetch(`${API_URL}/logs`);
  return res.json();
}

export async function fetchMetrics() {
  const res = await fetch(`${API_URL}/metrics`);
  return res.json();
}
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function sendChat(payload) {
  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}
