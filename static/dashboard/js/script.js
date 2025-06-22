document.addEventListener("DOMContentLoaded", () => {
  const html = document.documentElement;
  const themeToggle = document.getElementById("theme-toggle");
  const userbar = document.getElementById("userbar");
  const dropdown = document.getElementById("user-dropdown");
  const sidebarToggle = document.getElementById("sidebar-toggle");
  const sidebar = document.querySelector(".sidebar");

  // === Load saved theme from localStorage ===
  const savedTheme = localStorage.getItem("theme") || "light";
  html.setAttribute("data-theme", savedTheme);
  if (themeToggle) {
    themeToggle.textContent = savedTheme === "dark" ? "☀️" : "🌙";

    // === Toggle light/dark mode ===
    themeToggle.addEventListener("click", () => {
      const current = html.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      themeToggle.textContent = next === "dark" ? "☀️" : "🌙";
    });
  }

  // === Toggle user dropdown on avatar click ===
  if (userbar && dropdown) {
    userbar.addEventListener("click", (e) => {
      e.stopPropagation(); // Prevent event bubbling
      dropdown.classList.toggle("show");
    });

    document.addEventListener("click", (e) => {
      if (!userbar.contains(e.target)) {
        dropdown.classList.remove("show");
      }
    });
  }

  // === Sidebar toggle on mobile ===
  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener("click", () => {
      sidebar.classList.toggle("open");
    });
  }
});
