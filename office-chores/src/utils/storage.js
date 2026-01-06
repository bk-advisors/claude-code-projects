const STORAGE_KEYS = {
  CHORES: 'office-chores-data',
  TEAM: 'office-chores-team',
  CATEGORIES: 'office-chores-categories',
};

const DEFAULT_CATEGORIES = [
  { id: 'cleaning', name: 'Cleaning', color: '#4ADE80' },
  { id: 'maintenance', name: 'Maintenance', color: '#F59E0B' },
  { id: 'supplies', name: 'Supplies', color: '#3B82F6' },
  { id: 'admin', name: 'Administrative', color: '#8B5CF6' },
  { id: 'other', name: 'Other', color: '#6B7280' },
];

export function getChores() {
  try {
    const data = localStorage.getItem(STORAGE_KEYS.CHORES);
    return data ? JSON.parse(data) : [];
  } catch {
    return [];
  }
}

export function saveChores(chores) {
  localStorage.setItem(STORAGE_KEYS.CHORES, JSON.stringify(chores));
}

export function getTeamMembers() {
  try {
    const data = localStorage.getItem(STORAGE_KEYS.TEAM);
    return data ? JSON.parse(data) : [];
  } catch {
    return [];
  }
}

export function saveTeamMembers(members) {
  localStorage.setItem(STORAGE_KEYS.TEAM, JSON.stringify(members));
}

export function getCategories() {
  try {
    const data = localStorage.getItem(STORAGE_KEYS.CATEGORIES);
    return data ? JSON.parse(data) : DEFAULT_CATEGORIES;
  } catch {
    return DEFAULT_CATEGORIES;
  }
}

export function saveCategories(categories) {
  localStorage.setItem(STORAGE_KEYS.CATEGORIES, JSON.stringify(categories));
}
