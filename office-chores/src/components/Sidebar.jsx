import { useMemo } from 'react';
import { format, isToday, isTomorrow, isPast, startOfDay } from 'date-fns';
import { getOccurrencesInRange } from '../utils/recurrence';

export default function Sidebar({
  chores,
  categories,
  teamMembers,
  onAddChore,
  onManageTeam,
  onChoreClick,
  notificationStatus,
  onEnableNotifications,
}) {
  const upcomingChores = useMemo(() => {
    const today = startOfDay(new Date());
    const nextWeek = new Date(today);
    nextWeek.setDate(nextWeek.getDate() + 7);

    const allOccurrences = [];
    chores.forEach((chore) => {
      const occurrences = getOccurrencesInRange(chore, today, nextWeek);
      allOccurrences.push(...occurrences);
    });

    return allOccurrences
      .filter((c) => !c.completed)
      .sort((a, b) => new Date(a.occurrenceDate) - new Date(b.occurrenceDate))
      .slice(0, 5);
  }, [chores]);

  const stats = useMemo(() => {
    const today = startOfDay(new Date());
    const weekEnd = new Date(today);
    weekEnd.setDate(weekEnd.getDate() + 7);

    let total = 0;
    let completed = 0;
    let overdue = 0;

    chores.forEach((chore) => {
      const occurrences = getOccurrencesInRange(chore, today, weekEnd);
      occurrences.forEach((occ) => {
        total++;
        if (occ.completed) completed++;
        if (isPast(new Date(occ.occurrenceDate)) && !occ.completed) overdue++;
      });
    });

    return { total, completed, overdue };
  }, [chores]);

  const getCategoryColor = (categoryId) => {
    const category = categories.find((c) => c.id === categoryId);
    return category?.color || '#6B7280';
  };

  const formatDueDate = (date) => {
    const d = new Date(date);
    if (isToday(d)) return `Today, ${format(d, 'h:mm a')}`;
    if (isTomorrow(d)) return `Tomorrow, ${format(d, 'h:mm a')}`;
    return format(d, 'EEE, MMM d');
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div className="logo">
          <svg width="32" height="32" viewBox="0 0 100 100">
            <rect x="10" y="20" width="80" height="70" rx="5" fill="#4A90D9" stroke="#2E5A8A" strokeWidth="3"/>
            <rect x="10" y="20" width="80" height="15" rx="5" fill="#2E5A8A"/>
            <circle cx="30" cy="27" r="3" fill="#fff"/>
            <circle cx="70" cy="27" r="3" fill="#fff"/>
          </svg>
          <h1>Office Chores</h1>
        </div>
      </div>

      <div className="sidebar-actions">
        <button className="btn btn-primary btn-block" onClick={onAddChore}>
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M8 3V13M3 8H13" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
          </svg>
          Add Chore
        </button>
        <button className="btn btn-secondary btn-block" onClick={onManageTeam}>
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <circle cx="8" cy="5" r="3" stroke="currentColor" strokeWidth="1.5"/>
            <path d="M2 14C2 11.2386 4.23858 9 7 9H9C11.7614 9 14 11.2386 14 14" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
          </svg>
          Manage Team ({teamMembers.length})
        </button>
      </div>

      {notificationStatus !== 'granted' && notificationStatus !== 'unsupported' && (
        <div className="notification-banner">
          <p>Enable notifications to get reminders</p>
          <button className="btn btn-sm btn-secondary" onClick={onEnableNotifications}>
            Enable
          </button>
        </div>
      )}

      <div className="sidebar-stats">
        <h3>This Week</h3>
        <div className="stats-grid">
          <div className="stat">
            <span className="stat-value">{stats.total}</span>
            <span className="stat-label">Total</span>
          </div>
          <div className="stat">
            <span className="stat-value stat-success">{stats.completed}</span>
            <span className="stat-label">Done</span>
          </div>
          <div className="stat">
            <span className="stat-value stat-danger">{stats.overdue}</span>
            <span className="stat-label">Overdue</span>
          </div>
        </div>
      </div>

      <div className="sidebar-upcoming">
        <h3>Upcoming</h3>
        {upcomingChores.length === 0 ? (
          <p className="text-muted">No upcoming chores</p>
        ) : (
          <div className="upcoming-list">
            {upcomingChores.map((chore) => (
              <div
                key={chore.occurrenceId || chore.id}
                className="upcoming-item"
                onClick={() => onChoreClick(chore)}
              >
                <div
                  className="upcoming-category"
                  style={{ backgroundColor: getCategoryColor(chore.category) }}
                />
                <div className="upcoming-content">
                  <span className="upcoming-title">{chore.title}</span>
                  <span className="upcoming-date">{formatDueDate(chore.occurrenceDate)}</span>
                </div>
                {chore.recurrence && chore.recurrence !== 'none' && (
                  <span className="upcoming-recurring">↻</span>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="sidebar-categories">
        <h3>Categories</h3>
        <div className="category-list">
          {categories.map((cat) => (
            <div key={cat.id} className="category-item">
              <span className="category-dot" style={{ backgroundColor: cat.color }} />
              <span>{cat.name}</span>
            </div>
          ))}
        </div>
      </div>
    </aside>
  );
}
