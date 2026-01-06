import { useState } from 'react';

export default function TeamManager({ isOpen, onClose, teamMembers, onSave }) {
  const [members, setMembers] = useState(teamMembers);
  const [newMemberName, setNewMemberName] = useState('');

  const handleAddMember = (e) => {
    e.preventDefault();
    if (!newMemberName.trim()) return;

    const newMember = {
      id: crypto.randomUUID(),
      name: newMemberName.trim(),
    };

    setMembers([...members, newMember]);
    setNewMemberName('');
  };

  const handleRemoveMember = (id) => {
    setMembers(members.filter((m) => m.id !== id));
  };

  const handleSave = () => {
    onSave(members);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal modal-sm" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Team Members</h2>
          <button className="btn btn-icon" onClick={onClose}>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M15 5L5 15M5 5L15 15" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
            </svg>
          </button>
        </div>

        <div className="modal-body">
          <form onSubmit={handleAddMember} className="add-member-form">
            <input
              type="text"
              value={newMemberName}
              onChange={(e) => setNewMemberName(e.target.value)}
              placeholder="Enter team member name"
            />
            <button type="submit" className="btn btn-primary">
              Add
            </button>
          </form>

          <div className="team-list">
            {members.length === 0 ? (
              <p className="text-muted text-center">No team members yet</p>
            ) : (
              members.map((member) => (
                <div key={member.id} className="team-member">
                  <span className="member-avatar">
                    {member.name.charAt(0).toUpperCase()}
                  </span>
                  <span className="member-name">{member.name}</span>
                  <button
                    className="btn btn-icon btn-danger-ghost"
                    onClick={() => handleRemoveMember(member.id)}
                    title="Remove member"
                  >
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                      <path d="M12 4L4 12M4 4L12 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
                    </svg>
                  </button>
                </div>
              ))
            )}
          </div>

          <div className="modal-footer">
            <button className="btn btn-secondary" onClick={onClose}>
              Cancel
            </button>
            <button className="btn btn-primary" onClick={handleSave}>
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
