import React, { useState } from "react";
import { sendChat } from "./api";

export default function App() {
	const [userId, setUserId] = useState(1);
	const [question, setQuestion] = useState("");
	const [answer, setAnswer] = useState("");
	const [citations, setCitations] = useState([]);

	async function handleSend() {
		if (!question.trim()) return;
		const data = await sendChat({ user_id: userId, question });
		setAnswer(data.answer || "");
		setCitations(data.citations || []);
	}

	return (
		<div className="container">
			<h1>AI Helpdesk Chatbot</h1>
			<div className="row">
				<label>User ID</label>
				<select value={userId} onChange={(e) => setUserId(Number(e.target.value))}>
					<option value={1}>1 (Admin)</option>
					<option value={2}>2 (IT Agent)</option>
					<option value={3}>3 (Employee)</option>
				</select>
			</div>

			<textarea
				rows="4"
				placeholder="Ask a helpdesk question"
				value={question}
				onChange={(e) => setQuestion(e.target.value)}
			/>

			<button onClick={handleSend}>Send</button>

			<h2>Answer</h2>
			<p>{answer}</p>

			<h2>Citations</h2>
			<ul>
				{citations.map((c, i) => (
					<li key={i}>{c.title} — {c.chunk_id}</li>
				))}
			</ul>
		</div>
	);
}
