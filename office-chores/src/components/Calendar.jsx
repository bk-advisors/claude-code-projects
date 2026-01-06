import { useState, useMemo } from 'react';
import {
  startOfMonth,
  endOfMonth,
  startOfWeek,
  endOfWeek,
  eachDayOfInterval,
  format,
  isSameMonth,
  isSameDay,
  isToday,
  addMonths,
  subMonths,
} from 'date-fns';
import { getOccurrencesInRange } from '../utils/recurrence';

const PRIORITY_COLORS = {
  high: '#EF4444',
  medium: '#F59E0B',
  low: '#22C55E',
};

export default function Calendar({
  chores,
  categories,
  onDateClick,
  onChoreClick,
  selectedDate
}) {
  const [currentMonth, setCurrentMonth] = useState(new Date());

  const calendarDays = useMemo(() => {
    const monthStart = startOfMonth(currentMonth);
    const monthEnd = endOfMonth(currentMonth);
    const calendarStart = startOfWeek(monthStart, { weekStartsOn: 0 });
    const calendarEnd = endOfWeek(monthEnd, { weekStartsOn: 0 });

    return eachDayOfInterval({ start: calendarStart, end: calendarEnd });
  }, [currentMonth]);

  const choresByDate = useMemo(() => {
    const monthStart = startOfMonth(currentMonth);
    const monthEnd = endOfMonth(currentMonth);
    const calendarStart = startOfWeek(monthStart, { weekStartsOn: 0 });
    const calendarEnd = endOfWeek(monthEnd, { weekStartsOn: 0 });

    const map = new Map();

    chores.forEach((chore) => {
      const occurrences = getOccurrencesInRange(chore, calendarStart, calendarEnd);
      occurrences.forEach((occ) => {
        const dateKey = format(occ.occurrenceDate, 'yyyy-MM-dd');
        if (!map.has(dateKey)) {
          map.set(dateKey, []);
        }
        map.get(dateKey).push(occ);
      });
    });

    return map;
  }, [chores, currentMonth]);

  const getCategoryColor = (categoryId) => {
    const category = categories.find((c) => c.id === categoryId);
    return category?.color || '#6B7280';
  };

  const goToPreviousMonth = () => setCurrentMonth(subMonths(currentMonth, 1));
  const goToNextMonth = () => setCurrentMonth(addMonths(currentMonth, 1));
  const goToToday = () => setCurrentMonth(new Date());

  return (
    <div className="calendar">
      <div className="calendar-header">
        <button className="btn btn-icon" onClick={goToPreviousMonth}>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M12 15L7 10L12 5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </button>
        <div className="calendar-title">
          <h2>{format(currentMonth, 'MMMM yyyy')}</h2>
          <button className="btn btn-text" onClick={goToToday}>Today</button>
        </div>
        <button className="btn btn-icon" onClick={goToNextMonth}>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M8 5L13 10L8 15" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </button>
      </div>

      <div className="calendar-grid">
        <div className="calendar-weekdays">
          {['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].map((day) => (
            <div key={day} className="calendar-weekday">{day}</div>
          ))}
        </div>

        <div className="calendar-days">
          {calendarDays.map((day) => {
            const dateKey = format(day, 'yyyy-MM-dd');
            const dayChores = choresByDate.get(dateKey) || [];
            const isCurrentMonth = isSameMonth(day, currentMonth);
            const isSelected = selectedDate && isSameDay(day, selectedDate);

            return (
              <div
                key={dateKey}
                className={`calendar-day ${!isCurrentMonth ? 'other-month' : ''} ${isToday(day) ? 'today' : ''} ${isSelected ? 'selected' : ''}`}
                onClick={() => onDateClick(day)}
              >
                <span className="day-number">{format(day, 'd')}</span>
                <div className="day-chores">
                  {dayChores.slice(0, 3).map((chore) => (
                    <div
                      key={chore.occurrenceId || chore.id}
                      className={`chore-pill ${chore.completed ? 'completed' : ''}`}
                      style={{
                        borderLeftColor: getCategoryColor(chore.category),
                        '--priority-color': PRIORITY_COLORS[chore.priority] || PRIORITY_COLORS.medium
                      }}
                      onClick={(e) => {
                        e.stopPropagation();
                        onChoreClick(chore);
                      }}
                    >
                      <span className="chore-pill-priority" style={{ backgroundColor: PRIORITY_COLORS[chore.priority] || PRIORITY_COLORS.medium }}></span>
                      <span className="chore-pill-title">{chore.title}</span>
                      {chore.recurrence && chore.recurrence !== 'none' && (
                        <span className="chore-pill-recurring">↻</span>
                      )}
                    </div>
                  ))}
                  {dayChores.length > 3 && (
                    <div className="more-chores">+{dayChores.length - 3} more</div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
