# Office Chores

Office chore management app with calendar view, recurring tasks, team assignment, and browser notifications.

## Tech Stack

- **Framework**: React 18 with Vite 5
- **Date Handling**: date-fns v3
- **Persistence**: Browser localStorage (no backend)
- **Styling**: Plain CSS with CSS custom properties

## Project Structure

```
src/
├── main.jsx              # React entry point
├── App.jsx               # Root component, state management hub
├── index.css             # Global styles, CSS variables
├── components/
│   ├── Calendar.jsx      # Month view calendar grid
│   ├── ChoreModal.jsx    # Add/edit chore form modal
│   ├── Sidebar.jsx       # Navigation, stats, upcoming list
│   └── TeamManager.jsx   # Team member CRUD modal
└── utils/
    ├── storage.js        # localStorage get/save functions
    ├── recurrence.js     # Recurring chore occurrence logic
    └── notifications.js  # Browser notification API wrapper
```

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `src/components/` | React UI components (one component per file) |
| `src/utils/` | Pure utility functions, no React dependencies |
| `public/` | Static assets (favicon) |

## Commands

```bash
npm install     # Install dependencies
npm run dev     # Start dev server (http://localhost:5173)
npm run build   # Production build to dist/
npm run preview # Preview production build
```

## Data Models

**Chore** (see `src/components/ChoreModal.jsx:21-31`):
- `id`, `title`, `description`, `dueDate` (ISO string)
- `category`, `priority` (low/medium/high), `recurrence` (none/daily/weekly/monthly)
- `assignees` (array of names), `completed` (boolean)

**Team Member**: `{ id, name }`

**Category**: `{ id, name, color }` (defaults in `src/utils/storage.js:7-13`)

## Storage Keys

All data persisted to localStorage with keys defined in `src/utils/storage.js:1-5`:
- `office-chores-data` - Chores array
- `office-chores-team` - Team members array
- `office-chores-categories` - Categories array

## Additional Documentation

Check these files for specialized topics:

| Topic | File |
|-------|------|
| Architectural patterns & conventions | `.claude/docs/architectural_patterns.md` |
