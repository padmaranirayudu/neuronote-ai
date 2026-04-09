import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NeuroNote AI Voice Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 NeuroNote AI Voice Assistant")
st.caption("Voice task input + spoken reminders on smartphone browser")

html_code = r"""
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root{
      --bg:#0f172a;
      --card:#111827;
      --card2:#1f2937;
      --text:#f8fafc;
      --muted:#cbd5e1;
      --accent:#22c55e;
      --accent2:#38bdf8;
      --danger:#ef4444;
      --warn:#f59e0b;
      --border:#334155;
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family:Arial, Helvetica, sans-serif;
      background:linear-gradient(180deg,#0f172a 0%, #111827 100%);
      color:var(--text);
      padding:16px;
    }
    .wrap{
      max-width:980px;
      margin:0 auto;
    }
    .hero{
      background:linear-gradient(135deg,#111827,#1e293b);
      border:1px solid var(--border);
      border-radius:20px;
      padding:18px;
      margin-bottom:16px;
      box-shadow:0 12px 30px rgba(0,0,0,.25);
    }
    .hero h2{
      margin:0 0 8px 0;
      font-size:28px;
    }
    .hero p{
      margin:0;
      color:var(--muted);
      line-height:1.5;
    }
    .grid{
      display:grid;
      grid-template-columns:1.1fr 1fr;
      gap:16px;
    }
    @media (max-width: 860px){
      .grid{grid-template-columns:1fr}
    }
    .card{
      background:rgba(17,24,39,.95);
      border:1px solid var(--border);
      border-radius:20px;
      padding:16px;
      box-shadow:0 10px 25px rgba(0,0,0,.18);
    }
    .card h3{
      margin:0 0 12px 0;
      font-size:22px;
    }
    .muted{
      color:var(--muted);
      font-size:14px;
      line-height:1.5;
    }
    textarea, input, select{
      width:100%;
      background:#0b1220;
      color:var(--text);
      border:1px solid #3b475d;
      border-radius:14px;
      padding:12px 14px;
      font-size:16px;
      outline:none;
      margin-top:8px;
    }
    textarea{
      min-height:100px;
      resize:vertical;
    }
    .row{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:10px;
    }
    .btns{
      display:flex;
      flex-wrap:wrap;
      gap:10px;
      margin-top:12px;
    }
    button{
      border:none;
      border-radius:14px;
      padding:12px 16px;
      font-size:15px;
      font-weight:700;
      cursor:pointer;
      transition:.2s ease;
    }
    button:hover{
      transform:translateY(-1px);
      opacity:.95;
    }
    .primary{background:var(--accent); color:#06280f;}
    .secondary{background:var(--accent2); color:#062033;}
    .dark{background:#243042; color:var(--text);}
    .danger{background:var(--danger); color:white;}
    .warn{background:var(--warn); color:#311f00;}
    .pill{
      display:inline-block;
      padding:6px 10px;
      border-radius:999px;
      font-size:12px;
      font-weight:700;
      background:#0b1220;
      border:1px solid #334155;
      color:#cbd5e1;
      margin-right:6px;
      margin-top:6px;
    }
    .status{
      margin-top:12px;
      padding:12px 14px;
      border-radius:14px;
      background:#0b1220;
      border:1px solid #334155;
      color:#cbd5e1;
      min-height:48px;
      line-height:1.5;
    }
    .metrics{
      display:grid;
      grid-template-columns:repeat(4,1fr);
      gap:10px;
      margin-top:12px;
    }
    @media (max-width:700px){
      .metrics{grid-template-columns:repeat(2,1fr)}
    }
    .metric{
      background:#0b1220;
      border:1px solid var(--border);
      border-radius:16px;
      padding:14px;
    }
    .metric .num{
      font-size:28px;
      font-weight:800;
      margin-bottom:4px;
    }
    .task{
      background:#0b1220;
      border:1px solid var(--border);
      border-radius:16px;
      padding:14px;
      margin-top:12px;
    }
    .task-top{
      display:flex;
      align-items:flex-start;
      justify-content:space-between;
      gap:10px;
    }
    .task-title{
      font-size:18px;
      font-weight:800;
      margin:0 0 6px 0;
      line-height:1.4;
    }
    .task-sub{
      color:var(--muted);
      font-size:14px;
      line-height:1.5;
    }
    .task-actions{
      display:flex;
      gap:8px;
      flex-wrap:wrap;
      margin-top:12px;
    }
    .small{
      padding:9px 12px;
      border-radius:12px;
      font-size:13px;
    }
    .empty{
      color:var(--muted);
      text-align:center;
      padding:24px 10px;
      border:1px dashed #475569;
      border-radius:16px;
      margin-top:12px;
    }
    .good{color:#86efac}
    .overdue{color:#fca5a5}
    .soon{color:#fde68a}
    .footer-note{
      margin-top:16px;
      color:#94a3b8;
      font-size:13px;
      line-height:1.5;
    }
  </style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h2>🎤 Speak your task. ⏰ Hear the reminder.</h2>
    <p>
      Example: <b>“Remind me to call sir tomorrow at 5 PM”</b><br>
      This app listens, saves the task, and at the required time it gives:
      voice reminder, browser notification, and phone vibration when supported.
    </p>
  </div>

  <div class="grid">
    <div class="card">
      <h3>➕ Add Reminder</h3>
      <div class="muted">Use voice or type naturally.</div>

      <label style="display:block;margin-top:12px;">Natural language input</label>
      <textarea id="smartInput" placeholder="Example: Remind me to submit assignment tomorrow at 9 PM"></textarea>

      <div class="row">
        <div>
          <label style="display:block;margin-top:12px;">Priority</label>
          <select id="priority">
            <option>High</option>
            <option selected>Medium</option>
            <option>Low</option>
          </select>
        </div>
        <div>
          <label style="display:block;margin-top:12px;">Voice language</label>
          <select id="langSelect">
            <option value="en-IN" selected>English (India)</option>
            <option value="te-IN">Telugu (India)</option>
            <option value="en-US">English (US)</option>
          </select>
        </div>
      </div>

      <div class="btns">
        <button class="secondary" onclick="startListening()">🎙 Start Voice Input</button>
        <button class="primary" onclick="addSmartTask()">✅ Add Reminder</button>
        <button class="dark" onclick="requestNotify()">🔔 Enable Notifications</button>
        <button class="warn" onclick="testVoiceReminder()">🗣 Test Voice</button>
      </div>

      <div class="status" id="statusBox">Ready.</div>

      <div style="margin-top:12px;">
        <span class="pill">Voice input</span>
        <span class="pill">Spoken reminder</span>
        <span class="pill">Notification popup</span>
        <span class="pill">Phone vibration</span>
        <span class="pill">Browser local storage</span>
      </div>
    </div>

    <div class="card">
      <h3>📊 Assistant Summary</h3>
      <div class="metrics">
        <div class="metric">
          <div class="num" id="totalNum">0</div>
          <div>Total</div>
        </div>
        <div class="metric">
          <div class="num" id="pendingNum">0</div>
          <div>Pending</div>
        </div>
        <div class="metric">
          <div class="num" id="doneNum">0</div>
          <div>Done</div>
        </div>
        <div class="metric">
          <div class="num" id="overdueNum">0</div>
          <div>Overdue</div>
        </div>
      </div>

      <div class="footer-note">
        Best on smartphone Chrome. For stronger mobile experience:
        open in browser → tap 3 dots → <b>Add to Home Screen</b>.
        For the browser to speak on time, keep it open or recently active.
      </div>
    </div>
  </div>

  <div class="card" style="margin-top:16px;">
    <h3>📋 My Reminders</h3>
    <div id="taskList"></div>
  </div>
</div>

<script>
  const STORAGE_KEY = "neuronote_voice_tasks_v2";
  let tasks = loadTasks();

  function setStatus(msg){
    document.getElementById("statusBox").innerHTML = msg;
  }

  function saveTasks(){
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
  }

  function loadTasks(){
    try{
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    }catch(e){
      return [];
    }
  }

  function formatDateTime(ts){
    const d = new Date(ts);
    return d.toLocaleString([], {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "2-digit"
    });
  }

  function escapeHtml(str){
    return String(str)
      .replaceAll("&","&amp;")
      .replaceAll("<","&lt;")
      .replaceAll(">","&gt;")
      .replaceAll('"',"&quot;");
  }

  function getStatus(task){
    if(task.completed) return "Completed";
    const now = Date.now();
    const due = task.dueAt;
    if(due < now) return "Overdue";
    if(due - now <= 60 * 60 * 1000) return "Due Soon";
    return "Upcoming";
  }

  function updateMetrics(){
    const total = tasks.length;
    const done = tasks.filter(t => t.completed).length;
    const pending = tasks.filter(t => !t.completed).length;
    const overdue = tasks.filter(t => !t.completed && t.dueAt < Date.now()).length;

    document.getElementById("totalNum").innerText = total;
    document.getElementById("doneNum").innerText = done;
    document.getElementById("pendingNum").innerText = pending;
    document.getElementById("overdueNum").innerText = overdue;
  }

  function renderTasks(){
    const list = document.getElementById("taskList");
    if(!tasks.length){
      list.innerHTML = '<div class="empty">No reminders yet. Add your first voice reminder.</div>';
      updateMetrics();
      return;
    }

    tasks.sort((a,b) => {
      if(a.completed !== b.completed) return a.completed ? 1 : -1;
      return a.dueAt - b.dueAt;
    });

    list.innerHTML = tasks.map(task => {
      const status = getStatus(task);
      let statusClass = "";
      if(status === "Overdue") statusClass = "overdue";
      if(status === "Due Soon") statusClass = "soon";
      if(status === "Upcoming") statusClass = "good";

      return `
        <div class="task">
          <div class="task-top">
            <div>
              <div class="task-title">${task.completed ? "✅ " : ""}${escapeHtml(task.title)}</div>
              <div class="task-sub">
                Due: <b>${formatDateTime(task.dueAt)}</b><br>
                Priority: <b>${escapeHtml(task.priority)}</b> |
                Status: <b class="${statusClass}">${status}</b>
              </div>
            </div>
          </div>
          <div class="task-actions">
            ${task.completed ? "" : `<button class="small primary" onclick="markDone('${task.id}')">Done</button>`}
            <button class="small dark" onclick="speakNow('${escapeForJs(task.title)}', ${task.dueAt})">Speak</button>
            <button class="small danger" onclick="deleteTask('${task.id}')">Delete</button>
          </div>
        </div>
      `;
    }).join("");

    updateMetrics();
  }

  function escapeForJs(str){
    return String(str).replaceAll("\\", "\\\\").replaceAll("'", "\\'");
  }

  function deleteTask(id){
    tasks = tasks.filter(t => t.id !== id);
    saveTasks();
    renderTasks();
    setStatus("Reminder deleted.");
  }

  function markDone(id){
    tasks = tasks.map(t => t.id === id ? {...t, completed:true} : t);
    saveTasks();
    renderTasks();
    setStatus("Marked as completed.");
  }

  function requestNotify(){
    if(!("Notification" in window)){
      setStatus("This browser does not support notifications.");
      return;
    }
    Notification.requestPermission().then(permission => {
      setStatus("Notification permission: <b>" + permission + "</b>");
    });
  }

  function speakText(text){
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = document.getElementById("langSelect").value || "en-IN";
    utter.rate = 1;
    utter.pitch = 1;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utter);
  }

  function speakNow(title, dueAt){
    const msg = "Reminder. " + title + ". Scheduled for " + new Date(dueAt).toLocaleString();
    speakText(msg);
    setStatus("Speaking reminder: <b>" + escapeHtml(title) + "</b>");
  }

  function testVoiceReminder(){
    speakText("This is NeuroNote AI. Voice reminder is working correctly.");
    if(navigator.vibrate){
      navigator.vibrate([200,100,200]);
    }
    setStatus("Voice reminder test started.");
  }

  function notifyReminder(task){
    const message = "Reminder: " + task.title;

    if("Notification" in window && Notification.permission === "granted"){
      try{
        new Notification("NeuroNote AI", { body: message });
      }catch(e){}
    }

    if(navigator.vibrate){
      navigator.vibrate([300,150,300,150,300]);
    }

    speakText(message);
  }

  function parseNaturalReminder(inputText){
    const original = inputText.trim();
    const text = original.toLowerCase().trim();
    const now = new Date();

    let target = new Date();
    let foundDate = false;
    let foundTime = false;

    function setTime(hour, minute){
      target.setHours(hour, minute, 0, 0);
      foundTime = true;
    }

    let m;

    m = text.match(/\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b/);
    if(m){
      let hour = parseInt(m[1], 10);
      const minute = m[2] ? parseInt(m[2], 10) : 0;
      const ampm = m[3];
      if(hour === 12) hour = 0;
      if(ampm === "pm") hour += 12;
      setTime(hour, minute);
    } else {
      m = text.match(/\b(\d{1,2}):(\d{2})\b/);
      if(m){
        setTime(parseInt(m[1],10), parseInt(m[2],10));
      }
    }

    if(text.includes("today")){
      target = new Date();
      foundDate = true;
      if(foundTime){
        const tmp = new Date();
        tmp.setHours(target.getHours(), target.getMinutes(), 0, 0);
      }
    }

    if(text.includes("tomorrow")){
      target = new Date();
      target.setDate(target.getDate() + 1);
      foundDate = true;
    }

    m = text.match(/\bin\s+(\d+)\s+minutes?\b/);
    if(m){
      target = new Date(now.getTime() + parseInt(m[1],10) * 60000);
      foundDate = true;
      foundTime = true;
    }

    m = text.match(/\bin\s+(\d+)\s+hours?\b/);
    if(m){
      target = new Date(now.getTime() + parseInt(m[1],10) * 3600000);
      foundDate = true;
      foundTime = true;
    }

    m = text.match(/\b(\d{4})-(\d{1,2})-(\d{1,2})\b/);
    if(m){
      target = new Date(parseInt(m[1],10), parseInt(m[2],10)-1, parseInt(m[3],10));
      foundDate = true;
    }

    const weekdays = {
      sunday:0, monday:1, tuesday:2, wednesday:3,
      thursday:4, friday:5, saturday:6
    };

    Object.keys(weekdays).forEach(day => {
      const reg = new RegExp("\\\\b" + day + "\\\\b");
      if(reg.test(text)){
        let d = new Date();
        let diff = weekdays[day] - d.getDay();
        if(diff <= 0) diff += 7;
        d.setDate(d.getDate() + diff);
        if(foundTime){
          d.setHours(target.getHours(), target.getMinutes(), 0, 0);
        }
        target = d;
        foundDate = true;
      }
    });

    if(!foundTime){
      target.setHours(9, 0, 0, 0);
    }

    if(!foundDate && foundTime){
      const candidate = new Date();
      candidate.setHours(target.getHours(), target.getMinutes(), 0, 0);
      if(candidate.getTime() > Date.now()){
        target = candidate;
      } else {
        candidate.setDate(candidate.getDate() + 1);
        target = candidate;
      }
    }

    let title = original
      .replace(/remind me to/ig, "")
      .replace(/\btoday\b/ig, "")
      .replace(/\btomorrow\b/ig, "")
      .replace(/\bin\s+\d+\s+minutes?\b/ig, "")
      .replace(/\bin\s+\d+\s+hours?\b/ig, "")
      .replace(/\b(\d{4})-(\d{1,2})-(\d{1,2})\b/ig, "")
      .replace(/\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b/ig, "")
      .replace(/\b(\d{1,2}):(\d{2})\b/ig, "")
      .replace(/\bat\b/ig, "")
      .replace(/\bon\b/ig, "")
      .replace(/\bnext\b/ig, "")
      .replace(/\bmonday\b|\btuesday\b|\bwednesday\b|\bthursday\b|\bfriday\b|\bsaturday\b|\bsunday\b/ig, "")
      .replace(/\s+/g, " ")
      .trim()
      .replace(/^[,.\- ]+|[,.\- ]+$/g, "");

    if(!title) title = "Untitled reminder";

    return {
      title,
      dueAt: target.getTime()
    };
  }

  function addSmartTask(){
    const input = document.getElementById("smartInput").value.trim();
    const priority = document.getElementById("priority").value;

    if(!input){
      setStatus("Please enter or speak a reminder first.");
      return;
    }

    const parsed = parseNaturalReminder(input);

    const task = {
      id: "id_" + Date.now() + "_" + Math.random().toString(36).slice(2,8),
      title: parsed.title,
      dueAt: parsed.dueAt,
      priority: priority,
      completed: false,
      reminded: false,
      createdAt: Date.now()
    };

    tasks.push(task);
    saveTasks();
    renderTasks();

    document.getElementById("smartInput").value = "";

    setStatus(
      "Reminder added: <b>" + escapeHtml(task.title) +
      "</b><br>Due at: <b>" + formatDateTime(task.dueAt) + "</b>"
    );
  }

  function checkReminders(){
    const now = Date.now();
    let changed = false;

    tasks.forEach(task => {
      if(!task.completed && !task.reminded && now >= task.dueAt){
        notifyReminder(task);
        task.reminded = true;
        changed = true;
      }
    });

    if(changed){
      saveTasks();
      renderTasks();
    }
  }

  function startListening(){
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if(!SpeechRecognition){
      setStatus("Voice input not supported in this browser. Try Chrome on Android.");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = document.getElementById("langSelect").value || "en-IN";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    setStatus("Listening... Speak now.");

    recognition.onresult = function(event){
      const transcript = event.results[0][0].transcript;
      document.getElementById("smartInput").value = transcript;
      setStatus("Voice captured: <b>" + escapeHtml(transcript) + "</b>");
    };

    recognition.onerror = function(event){
      setStatus("Voice input error: " + escapeHtml(event.error));
    };

    recognition.onend = function(){};

    recognition.start();
  }

  renderTasks();
  setInterval(checkReminders, 1000);
</script>
</body>
</html>
"""

components.html(html_code, height=980, scrolling=True)

st.info(
    "Important: For a smartphone browser MVP, this is strong. "
    "For a true background assistant that reminds you with voice even when the phone is locked, "
    "the next step is a native Android app."
)
