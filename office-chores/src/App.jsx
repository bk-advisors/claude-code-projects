import { useState, useEffect, useCallback } from 'react';
import Calendar from './components/Calendar';
import ChoreModal from './components/ChoreModal';
import TeamManager from './components/TeamManager';
import Sidebar from './components/Sidebar';
import {
  getChores,
  saveChores,
  getTeamMembers,
  saveTeamMembers,
  getCategories,
} from './utils/storage';
import {
  requestNotificationPermission,
  getNotificationStatus,
  scheduleChoreReminder,
} from './utils/notifications';

export default function App() {
  const [chores, setChores] = useState([]);
  const [teamMembers, setTeamMembers] = useState([]);
  const [categories] = useState(getCategories());
  const [selectedDate, setSelectedDate] = useState(null);
  const [selectedChore, setSelectedChore] = useState(null);
  const [isChoreModalOpen, setIsChoreModalOpen] = useState(false);
  const [isTeamModalOpen, setIsTeamModalOpen] = useState(false);
  const [notificationStatus, setNotificationStatus] = useState('default');
  const [reminderTimeouts, setReminderTimeouts] = useState([]);

  // Load data on mount
  useEffect(() => {
    setChores(getChores());
    setTeamMembers(getTeamMembers());
    setNotificationStatus(getNotificationStatus());
  }, []);

  // Schedule notifications for upcoming chores
  useEffect(() => {
    // Clear existing timeouts
    reminderTimeouts.forEach((timeout) => clearTimeout(timeout));

    if (notificationStatus === 'granted') {
      const newTimeouts = [];
      chores.forEach((chore) => {
        if (!chore.completed) {
          const timeout = scheduleChoreReminder(chore, 30);
          if (timeout) newTimeouts.push(timeout);
        }
      });
      setReminderTimeouts(newTimeouts);
    }

    return () => {
      reminderTimeouts.forEach((timeout) => clearTimeout(timeout));
    };
  }, [chores, notificationStatus]);

  const handleEnableNotifications = async () => {
    const granted = await requestNotificationPermission();
    setNotificationStatus(granted ? 'granted' : 'denied');
  };

  const handleDateClick = useCallback((date) => {
    setSelectedDate(date);
    setSelectedChore(null);
    setIsChoreModalOpen(true);
  }, []);

  const handleChoreClick = useCallback((chore) => {
    setSelectedChore(chore);
    setSelectedDate(null);
    setIsChoreModalOpen(true);
  }, []);

  const handleSaveChore = useCallback((choreData) => {
    setChores((prev) => {
      let newChores;
      if (choreData.id) {
        // Update existing chore
        newChores = prev.map((c) => (c.id === choreData.id ? { ...c, ...choreData } : c));
      } else {
        // Add new chore
        newChores = [...prev, { ...choreData, id: crypto.randomUUID() }];
      }
      saveChores(newChores);
      return newChores;
    });
    setIsChoreModalOpen(false);
    setSelectedChore(null);
    setSelectedDate(null);
  }, []);

  const handleDeleteChore = useCallback((choreId) => {
    setChores((prev) => {
      const newChores = prev.filter((c) => c.id !== choreId);
      saveChores(newChores);
      return newChores;
    });
    setIsChoreModalOpen(false);
    setSelectedChore(null);
  }, []);

  const handleSaveTeam = useCallback((members) => {
    setTeamMembers(members);
    saveTeamMembers(members);
  }, []);

  const handleAddChore = useCallback(() => {
    setSelectedDate(new Date());
    setSelectedChore(null);
    setIsChoreModalOpen(true);
  }, []);

  return (
    <div className="app">
      <Sidebar
        chores={chores}
        categories={categories}
        teamMembers={teamMembers}
        onAddChore={handleAddChore}
        onManageTeam={() => setIsTeamModalOpen(true)}
        onChoreClick={handleChoreClick}
        notificationStatus={notificationStatus}
        onEnableNotifications={handleEnableNotifications}
      />

      <main className="main-content">
        <Calendar
          chores={chores}
          categories={categories}
          selectedDate={selectedDate}
          onDateClick={handleDateClick}
          onChoreClick={handleChoreClick}
        />
      </main>

      <ChoreModal
        isOpen={isChoreModalOpen}
        onClose={() => {
          setIsChoreModalOpen(false);
          setSelectedChore(null);
          setSelectedDate(null);
        }}
        onSave={handleSaveChore}
        onDelete={handleDeleteChore}
        chore={selectedChore}
        categories={categories}
        teamMembers={teamMembers}
        selectedDate={selectedDate}
      />

      <TeamManager
        isOpen={isTeamModalOpen}
        onClose={() => setIsTeamModalOpen(false)}
        teamMembers={teamMembers}
        onSave={handleSaveTeam}
      />
    </div>
  );
}
