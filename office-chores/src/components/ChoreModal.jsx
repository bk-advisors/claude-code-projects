import { useState, useEffect } from 'react';
import { format } from 'date-fns';
import { RECURRENCE_TYPES } from '../utils/recurrence';

const PRIORITY_OPTIONS = [
  { value: 'low', label: 'Low', color: '#22C55E' },
  { value: 'medium', label: 'Medium', color: '#F59E0B' },
  { value: 'high', label: 'High', color: '#EF4444' },
];

export default function ChoreModal({
  isOpen,
  onClose,
  onSave,
  onDelete,
  chore,
  categories,
  teamMembers,
  selectedDate,
}) {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    dueDate: format(new Date(), 'yyyy-MM-dd'),
    dueTime: '09:00',
    category: 'other',
    priority: 'medium',
    recurrence: RECURRENCE_TYPES.NONE,
    assignees: [],
    completed: false,
  });

  useEffect(() => {
    if (chore) {
      const dueDate = new Date(chore.dueDate);
      setFormData({
        title: chore.title || '',
        description: chore.description || '',
        dueDate: format(dueDate, 'yyyy-MM-dd'),
        dueTime: format(dueDate, 'HH:mm'),
        category: chore.category || 'other',
        priority: chore.priority || 'medium',
        recurrence: chore.recurrence || RECURRENCE_TYPES.NONE,
        assignees: chore.assignees || [],
        completed: chore.completed || false,
      });
    } else if (selectedDate) {
      setFormData((prev) => ({
        ...prev,
        title: '',
        description: '',
        dueDate: format(selectedDate, 'yyyy-MM-dd'),
        dueTime: '09:00',
        category: 'other',
        priority: 'medium',
        recurrence: RECURRENCE_TYPES.NONE,
        assignees: [],
        completed: false,
      }));
    }
  }, [chore, selectedDate, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title.trim()) return;

    const dueDateTime = new Date(`${formData.dueDate}T${formData.dueTime}`);

    onSave({
      id: chore?.id,
      title: formData.title.trim(),
      description: formData.description.trim(),
      dueDate: dueDateTime.toISOString(),
      category: formData.category,
      priority: formData.priority,
      recurrence: formData.recurrence,
      assignees: formData.assignees,
      completed: formData.completed,
    });
  };

  const handleAssigneeToggle = (memberName) => {
    setFormData((prev) => ({
      ...prev,
      assignees: prev.assignees.includes(memberName)
        ? prev.assignees.filter((a) => a !== memberName)
        : [...prev.assignees, memberName],
    }));
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{chore ? 'Edit Chore' : 'New Chore'}</h2>
          <button className="btn btn-icon" onClick={onClose}>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M15 5L5 15M5 5L15 15" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
            </svg>
          </button>
        </div>

        <form onSubmit={handleSubmit} className="modal-body">
          <div className="form-group">
            <label htmlFor="title">Title *</label>
            <input
              id="title"
              type="text"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              placeholder="Enter chore title"
              autoFocus
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="description">Description</label>
            <textarea
              id="description"
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              placeholder="Add details about this chore"
              rows={3}
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="dueDate">Due Date</label>
              <input
                id="dueDate"
                type="date"
                value={formData.dueDate}
                onChange={(e) => setFormData({ ...formData, dueDate: e.target.value })}
              />
            </div>
            <div className="form-group">
              <label htmlFor="dueTime">Time</label>
              <input
                id="dueTime"
                type="time"
                value={formData.dueTime}
                onChange={(e) => setFormData({ ...formData, dueTime: e.target.value })}
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="category">Category</label>
              <select
                id="category"
                value={formData.category}
                onChange={(e) => setFormData({ ...formData, category: e.target.value })}
              >
                {categories.map((cat) => (
                  <option key={cat.id} value={cat.id}>
                    {cat.name}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="priority">Priority</label>
              <select
                id="priority"
                value={formData.priority}
                onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
              >
                {PRIORITY_OPTIONS.map((opt) => (
                  <option key={opt.value} value={opt.value}>
                    {opt.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="recurrence">Recurrence</label>
            <select
              id="recurrence"
              value={formData.recurrence}
              onChange={(e) => setFormData({ ...formData, recurrence: e.target.value })}
            >
              <option value={RECURRENCE_TYPES.NONE}>No recurrence</option>
              <option value={RECURRENCE_TYPES.DAILY}>Daily</option>
              <option value={RECURRENCE_TYPES.WEEKLY}>Weekly</option>
              <option value={RECURRENCE_TYPES.MONTHLY}>Monthly</option>
            </select>
          </div>

          <div className="form-group">
            <label>Assign to</label>
            {teamMembers.length === 0 ? (
              <p className="text-muted">No team members added yet</p>
            ) : (
              <div className="assignee-list">
                {teamMembers.map((member) => (
                  <label key={member.id} className="assignee-checkbox">
                    <input
                      type="checkbox"
                      checked={formData.assignees.includes(member.name)}
                      onChange={() => handleAssigneeToggle(member.name)}
                    />
                    <span>{member.name}</span>
                  </label>
                ))}
              </div>
            )}
          </div>

          {chore && (
            <div className="form-group">
              <label className="assignee-checkbox">
                <input
                  type="checkbox"
                  checked={formData.completed}
                  onChange={(e) => setFormData({ ...formData, completed: e.target.checked })}
                />
                <span>Mark as completed</span>
              </label>
            </div>
          )}

          <div className="modal-footer">
            {chore && (
              <button
                type="button"
                className="btn btn-danger"
                onClick={() => onDelete(chore.id)}
              >
                Delete
              </button>
            )}
            <div className="modal-actions">
              <button type="button" className="btn btn-secondary" onClick={onClose}>
                Cancel
              </button>
              <button type="submit" className="btn btn-primary">
                {chore ? 'Save Changes' : 'Add Chore'}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}
