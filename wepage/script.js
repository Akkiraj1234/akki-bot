fetch("https://github.com/Akkiraj1234/akki-bot/blob/main/resource/data.json?raw=true")
  .then((res) => {
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    return res.json();
  })
  .then((data) => {
    const {
      botName,
      botDesc,
      botLogo: { path: logoPath, alt: logoAlt, width: logoW, height: logoH },
      socials,
      features,
      commands,
      links: { invite, email, github, site },
      stats
    } = data;

    // Header
    document.getElementById("bot-name").textContent = botName;
    document.getElementById("bot-desc").textContent = botDesc;
    const logoDiv = document.getElementById("logo");
    logoDiv.innerHTML = "";
    const img = document.createElement("img");
    img.src = logoPath;
    img.alt = logoAlt;
    img.width = logoW;
    img.height = logoH;
    img.style.objectFit = "contain";
    img.style.borderRadius = "50%";
    logoDiv.appendChild(img);
    document.getElementById("invite-btn")
      .addEventListener("click", () => window.open(invite, "_blank"));

    // Socials
    const socialsContainer = document.getElementById("socials-container");
    socialsContainer.innerHTML = "";
    socials.forEach(({ icon, url }) => {
      const a = document.createElement("a");
      a.href = url;
      a.target = "_blank";
      a.innerHTML = `<ion-icon name="${icon}"></ion-icon>`;
      socialsContainer.appendChild(a);
    });

    // Stats
    const statsContainer = document.getElementById("stats-container");
    statsContainer.innerHTML = "";
    stats.forEach(({ key, value }) => {
      const div = document.createElement("div");
      div.className = "stat-item";
      div.textContent = `${key}: ${value}`;
      statsContainer.appendChild(div);
    });

    // Features
    const flist = document.getElementById("features-list");
    flist.innerHTML = "";
    features.forEach((text) => {
      const li = document.createElement("li");
      li.textContent = text;
      flist.appendChild(li);
    });

    // Commands (split ! + name, then description)
    const clist = document.getElementById("commands-list");
    clist.innerHTML = "";
    commands.forEach(({ cmd, desc }) => {
      const row = document.createElement("div");
      row.classList.add("command-row");

      const opPart   = cmd.charAt(0);   // "!"
      const namePart = cmd.slice(1);    // e.g. "setgithub"

      const cmdFull = document.createElement("span");
      cmdFull.className = "cmd-full";
      cmdFull.innerHTML =
        `<span class="cmd-op">${opPart}</span>` +
        `<span class="cmd-name">${namePart}</span>`;

      const descSpan = document.createElement("span");
      descSpan.className = "cmd-desc";
      descSpan.textContent = desc;

      row.append(cmdFull, descSpan);
      clist.appendChild(row);
    });

    // Footer links
    document.getElementById("email-link").href = email;
    document.getElementById("github-link").href = github;
    document.getElementById("site-link").href = site;
  })
  .catch((err) => console.error("Failed to load data.json:", err));
