function showToast(title, message = '', type = 'info', duration = 3000) {
  const toast = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');

  if (!toast) return;

  // Reset all type-specific classes
  toast.classList.remove(
    'border-green-500', 'bg-green-50',
    'border-red-500', 'bg-red-50',
    'border-blue-500', 'bg-blue-50',
    'border-gray-300', 'bg-white/90'
  );

  // Set default icon & color based on type
  let icon = '';
  if (type === 'success') {
    toast.classList.add('border-green-500', 'bg-green-50');
    icon = '✅';
  } else if (type === 'error') {
    toast.classList.add('border-red-500', 'bg-red-50');
    icon = '❌';
  } else if (type === 'warning') {
    toast.classList.add('border-yellow-500', 'bg-yellow-50');
    icon = '⚠️';
  } else {
    toast.classList.add('border-blue-500', 'bg-blue-50');
    icon = 'ℹ️';
  }

  // Update content
  toastTitle.textContent = title;
  toastMessage.textContent = message;
  toastIcon.textContent = icon;

  // Show animation
  toast.classList.remove('opacity-0', 'translate-y-10', 'scale-95');
  toast.classList.add('opacity-100', 'translate-y-0', 'scale-100');

  // Auto-hide after duration
  clearTimeout(window.toastTimeout);
  window.toastTimeout = setTimeout(() => {
    hideToast();
  }, duration);
}

function hideToast() {
  const toast = document.getElementById('toast-component');
  if (!toast) return;

  toast.classList.remove('opacity-100', 'translate-y-0', 'scale-100');
  toast.classList.add('opacity-0', 'translate-y-10', 'scale-95');
}