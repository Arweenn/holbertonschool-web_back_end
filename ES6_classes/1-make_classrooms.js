import ClassRoom from './0-classroom';

function initializeRooms() {
  const roomA = new ClassRoom(19);
  const roomB = new ClassRoom(20);
  const roomC = new ClassRoom(34);

  return [roomA, roomB, roomC];
}

export default initializeRooms;
