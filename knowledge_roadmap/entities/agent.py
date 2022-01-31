from knowledge_roadmap.entities.knowledge_road_map import KnowledgeRoadmap


class Agent():
    ''' 
    The goal of this method is to
    - be an adapter for sending commands to the spot robot.
    '''

    def __init__(self, start_pos:tuple, debug=False) -> None:
        self.debug = debug
        self.at_wp = 0
        self.pos = start_pos
        self.previous_pos = self.pos
        self.agent_drawing = None
        self.local_grid_drawing = None
        self.no_more_frontiers = False
        self.steps_taken = 0

    def teleport_to_pos(self, pos:tuple) -> None:
        '''
        Teleport the agent to a new position.
        
        :param pos: the position of the agent
        :return: None
        '''
        # TODO: add a check to see if the position is within the navigation radius.
        self.previous_pos = self.pos
        self.pos = pos
        self.steps_taken += 1

    # FIXME: remove KRM dependency
    def perform_path_step(self, path:list, krm:KnowledgeRoadmap) -> list or None:
        '''
        Execute a single step of the path.
        '''
        if self.debug:
            print(f"the path {path} length is {len(path)}")
        if len(path) > 1:
            node_data = krm.get_node_data_by_idx(path[0])
            self.teleport_to_pos(node_data['pos'])
            path.pop(0)
            return path

        elif len(path) == 1:
            selected_frontier_data = krm.get_node_data_by_idx(
                path[0])
            self.teleport_to_pos(selected_frontier_data['pos'])
            if self.debug:
                print(f"SELECTED FRONTIER POS {selected_frontier_data['pos']}")
            return None
