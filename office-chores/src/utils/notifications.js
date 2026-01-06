export async function requestNotificationPermission() {
  if (!('Notification' in window)) {
    console.log('This browser does not support notifications');
    return false;
  }

  if (Notification.permission === 'granted') {
    return true;
  }

  if (Notification.permission !== 'denied') {
    const permission = await Notification.requestPermission();
    return permission === 'granted';
  }

  return false;
}

export function sendNotification(title, options = {}) {
  if (Notification.permission === 'granted') {
    const notification = new Notification(title, {
      icon: '/favicon.svg',
      badge: '/favicon.svg',
      ...options,
    });

    notification.onclick = () => {
      window.focus();
      notification.close();
    };

    return notification;
  }
  return null;
}

export function scheduleChoreReminder(chore, minutesBefore = 30) {
  const dueDate = new Date(chore.dueDate);
  const reminderTime = new Date(dueDate.getTime() - minutesBefore * 60 * 1000);
  const now = new Date();

  if (reminderTime > now) {
    const timeout = reminderTime.getTime() - now.getTime();

    return setTimeout(() => {
      sendNotification(`Chore Reminder: ${chore.title}`, {
        body: `Due in ${minutesBefore} minutes. Assigned to: ${chore.assignees.join(', ') || 'Unassigned'}`,
        tag: chore.id,
      });
    }, timeout);
  }
  return null;
}

export function getNotificationStatus() {
  if (!('Notification' in window)) {
    return 'unsupported';
  }
  return Notification.permission;
}
