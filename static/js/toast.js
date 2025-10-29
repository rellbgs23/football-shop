const toastTypes = {
    success: {
        // switched success color to blue to match AJAX UI updates
        bg: "bg-blue-500",
    },
    error: {
        bg: "bg-red-500",
    },
    warning: {
        bg: "bg-yellow-500 text-black",
    },
    info: {
        bg: "bg-blue-500",
    }
};

function showToast(title, message, type = "info", duration = 2000) {
    const toastWrapper = document.getElementById("toast-wrapper");
    const toast = document.createElement("div");

    const { bg } = toastTypes[type] || toastTypes.info;

    toast.className = `
        flex items-start gap-3 p-4 rounded-lg shadow-lg text-white w-72
        opacity-0 translate-y-4 transition-all duration-300 cursor-pointer
        ${bg}
    `;

    toast.innerHTML = `
        <div class="flex-1">
            <h3 class="font-semibold">${title}</h3>
            <p class="text-sm opacity-90">${message}</p>
        </div>
    `;

    toastWrapper.appendChild(toast);

    // animate in
    requestAnimationFrame(() => {
        toast.classList.remove("opacity-0", "translate-y-4");
        toast.classList.add("opacity-100", "translate-y-0");
    });

    // hover pause
    let hideTimeout = setTimeout(removeToast, duration);
    toast.addEventListener("mouseenter", () => clearTimeout(hideTimeout));
    toast.addEventListener("mouseleave", () => {
        hideTimeout = setTimeout(removeToast, duration);
    });

    function removeToast() {
        toast.classList.add("opacity-0", "translate-y-4");
        toast.classList.remove("opacity-100");
        setTimeout(() => toast.remove(), 300);
    }

    // click to dismiss
    toast.addEventListener("click", removeToast);
}
