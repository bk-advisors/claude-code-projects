import { addDays, addWeeks, addMonths, isSameDay, startOfDay, endOfDay, isWithinInterval } from 'date-fns';

export const RECURRENCE_TYPES = {
  NONE: 'none',
  DAILY: 'daily',
  WEEKLY: 'weekly',
  MONTHLY: 'monthly',
};

export function getNextOccurrence(baseDate, recurrenceType, afterDate = new Date()) {
  const base = new Date(baseDate);
  let current = new Date(base);

  while (current <= afterDate) {
    switch (recurrenceType) {
      case RECURRENCE_TYPES.DAILY:
        current = addDays(current, 1);
        break;
      case RECURRENCE_TYPES.WEEKLY:
        current = addWeeks(current, 1);
        break;
      case RECURRENCE_TYPES.MONTHLY:
        current = addMonths(current, 1);
        break;
      default:
        return null;
    }
  }

  return current;
}

export function getOccurrencesInRange(chore, startDate, endDate) {
  if (chore.recurrence === RECURRENCE_TYPES.NONE || !chore.recurrence) {
    const choreDate = new Date(chore.dueDate);
    if (isWithinInterval(choreDate, { start: startOfDay(startDate), end: endOfDay(endDate) })) {
      return [{ ...chore, occurrenceDate: choreDate }];
    }
    return [];
  }

  const occurrences = [];
  let current = new Date(chore.dueDate);
  const rangeStart = startOfDay(startDate);
  const rangeEnd = endOfDay(endDate);

  // Move to first occurrence at or after range start
  while (current < rangeStart) {
    switch (chore.recurrence) {
      case RECURRENCE_TYPES.DAILY:
        current = addDays(current, 1);
        break;
      case RECURRENCE_TYPES.WEEKLY:
        current = addWeeks(current, 1);
        break;
      case RECURRENCE_TYPES.MONTHLY:
        current = addMonths(current, 1);
        break;
    }
  }

  // Collect all occurrences within range
  while (current <= rangeEnd) {
    occurrences.push({
      ...chore,
      occurrenceDate: new Date(current),
      occurrenceId: `${chore.id}-${current.toISOString()}`,
    });

    switch (chore.recurrence) {
      case RECURRENCE_TYPES.DAILY:
        current = addDays(current, 1);
        break;
      case RECURRENCE_TYPES.WEEKLY:
        current = addWeeks(current, 1);
        break;
      case RECURRENCE_TYPES.MONTHLY:
        current = addMonths(current, 1);
        break;
      default:
        break;
    }
  }

  return occurrences;
}

export function isChoreOnDate(chore, date) {
  const choreDate = new Date(chore.dueDate);

  if (chore.recurrence === RECURRENCE_TYPES.NONE || !chore.recurrence) {
    return isSameDay(choreDate, date);
  }

  let current = new Date(choreDate);
  const checkDate = startOfDay(date);

  while (current <= checkDate) {
    if (isSameDay(current, checkDate)) {
      return true;
    }

    switch (chore.recurrence) {
      case RECURRENCE_TYPES.DAILY:
        current = addDays(current, 1);
        break;
      case RECURRENCE_TYPES.WEEKLY:
        current = addWeeks(current, 1);
        break;
      case RECURRENCE_TYPES.MONTHLY:
        current = addMonths(current, 1);
        break;
      default:
        return false;
    }
  }

  return false;
}
