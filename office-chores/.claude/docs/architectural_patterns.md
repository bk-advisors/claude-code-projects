# Architectural Patterns

## State Management: Centralized in App

All application state lives in `src/App.jsx:20-28`. Child components receive data via props and communicate changes through callback props (`onX` pattern).

**Pattern**: App owns state, children are presentational
- State: `chores`, `teamMembers`, `categories`, modal visibility flags
- Callbacks: `handleSaveChore`, `handleDeleteChore`, `handleSaveTeam`

**Examples**:
- `src/App.jsx:116-125` - Sidebar receives `chores`, `onAddChore`, `onChoreClick`
- `src/App.jsx:137-150` - ChoreModal receives `onSave`, `onDelete`, `onClose`

## Event Handling: Callback Props

Components expose events via `onX` props. Parent handles business logic and state updates.

**Pattern**: `on{Action}` naming for callbacks
- `onDateClick`, `onChoreClick` - user interactions
- `onSave`, `onDelete`, `onClose` - CRUD operations

**Examples**:
- `src/components/Calendar.jsx:109` - `onClick={() => onDateClick(day)}`
- `src/components/ChoreModal.jsx:69-79` - `onSave` called with form data

## Controlled Modals

Modals are controlled components with `isOpen` prop. State resets when modal opens via `useEffect`.

**Pattern**: `isOpen` + `useEffect` for form reset
- `src/components/ChoreModal.jsx:33-61` - Reset form when `chore`, `selectedDate`, or `isOpen` changes
- `src/components/ChoreModal.jsx:91` - Early return if `!isOpen`

**Overlay click to close**:
- `src/components/ChoreModal.jsx:94` - `onClick={onClose}` on overlay
- `src/components/ChoreModal.jsx:95` - `e.stopPropagation()` on modal content

## Memoized Derived Data

Use `useMemo` for expensive computations derived from props/state.

**Pattern**: Compute once, re-compute only when dependencies change
- `src/components/Calendar.jsx:32-39` - `calendarDays` from `currentMonth`
- `src/components/Calendar.jsx:41-61` - `choresByDate` Map from `chores` + `currentMonth`
- `src/components/Sidebar.jsx:15-30` - `upcomingChores` filtered and sorted
- `src/components/Sidebar.jsx:32-51` - `stats` aggregation

## Utility Module Pattern

Pure functions in `src/utils/` with no React dependencies. Each module handles one concern.

**Pattern**: Export named functions, keep modules focused
- `storage.js` - `getX()` / `saveX()` pairs for each entity type
- `recurrence.js` - `getOccurrencesInRange()`, `isChoreOnDate()`, `getNextOccurrence()`
- `notifications.js` - `requestNotificationPermission()`, `sendNotification()`, `scheduleChoreReminder()`

**Error handling**: Try/catch with fallback defaults
- `src/utils/storage.js:15-22` - Returns `[]` on parse error

## Occurrence-Based Recurrence

Recurring chores stored as single record; occurrences generated on-demand for display.

**Pattern**: Base chore + recurrence type -> occurrence instances
- `src/utils/recurrence.js:33-86` - `getOccurrencesInRange()` generates virtual occurrences
- Each occurrence gets `occurrenceDate` and unique `occurrenceId`
- `src/components/Calendar.jsx:49-57` - Build `choresByDate` Map from occurrences

## Color Constants

Colors defined as module-level constants, not in CSS.

**Pattern**: Object literals for color mappings
- `src/components/Calendar.jsx:17-21` - `PRIORITY_COLORS`
- `src/components/ChoreModal.jsx:5-9` - `PRIORITY_OPTIONS` with colors
- `src/utils/storage.js:7-13` - `DEFAULT_CATEGORIES` with colors

## CSS Architecture

Single global stylesheet with CSS custom properties for theming.

**Pattern**: BEM-like class naming, CSS variables for colors
- Variables defined in `src/index.css:4-23`
- Component-scoped class names: `.calendar`, `.calendar-header`, `.calendar-day`
- Modifier classes: `.other-month`, `.today`, `.selected`, `.completed`
