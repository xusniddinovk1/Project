document.addEventListener("DOMContentLoaded", () => {
  const toggleSidebarBtn = document.querySelector(".toggle-sidebar");
  const toggleThemeBtn = document.querySelector(".toggle-theme");
  const sidebar = document.querySelector(".sidebar");
  const html = document.documentElement;

  const username = document.getElementById("username");
  const dropdown = document.getElementById("user-dropdown");

  // Restore theme
  const savedTheme = localStorage.getItem("theme") || "light";
  html.setAttribute("data-theme", savedTheme);
  toggleThemeBtn.textContent = savedTheme === "dark" ? "☀️" : "🌙";

  // Sidebar toggle — faqat bo‘lsa ishlaydi
  if (toggleSidebarBtn && sidebar) {
    toggleSidebarBtn.addEventListener("click", () => {
      sidebar.classList.toggle("open");
    });
  }

  // Theme toggle
  if (toggleThemeBtn) {
    toggleThemeBtn.addEventListener("click", () => {
      const current = html.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      toggleThemeBtn.textContent = next === "dark" ? "☀️" : "🌙";
    });
  }

  // Dropdown for username
  if (username && dropdown) {
    username.addEventListener("click", (e) => {
      e.stopPropagation();
      dropdown.classList.toggle("open");
    });

    document.addEventListener("click", () => {
      dropdown.classList.remove("open");
    });
  }
});
