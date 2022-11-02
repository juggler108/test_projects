class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.list_tracks = []

    def __len__(self):
        distance = 0
        x1, y1 = self.start_x, self.start_y
        for obj in self.list_tracks:
            x2, y2 = obj.to_x, obj.to_y
            distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            x1, y1 = x2, y2
        return int(distance)

    def verify_data(self, other):
        if not isinstance(other, Track):
            raise TypeError('Right operand must be Track type')

        return other

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.__len__() == sc.__len__()

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.__len__() < sc.__len__()

    def add_track(self, tr):
        self.list_tracks.append(tr)

    def get_tracks(self):
        return tuple(self.list_tracks)


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2