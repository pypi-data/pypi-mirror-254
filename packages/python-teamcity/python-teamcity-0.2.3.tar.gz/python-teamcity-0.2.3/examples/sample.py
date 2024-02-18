import logging
import os
import re

from teamcity import TeamCity

TEAMCITY_SERVER = os.environ.get('TEAMCITY_SERVER', None)
TEAMCITY_TOKENS = os.environ.get('TEAMCITY_TOKENS', None)

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    tc = TeamCity(server=TEAMCITY_SERVER, tokens=TEAMCITY_TOKENS)
    # s = tc.get_build_details(1)
    # print(tc.get_build_details(23929740))
    # print(tc.get_all_builds(build_type_id='Hk4eAsset_Streaming_38devAssignerTools'))
    # single = tc.get_builds_by_since_build(25954043,count = 50)
    agent_data = tc.get_all_agents(True)
    streaming_agent_build = []
    for agent in agent_data:
        if agent.get('pool', {}).get('name', '') == 'Streaming' and re.match(r'^Streaming', agent.get('name')):
            streaming_agent_build.append({'agent_id': agent.get('id'),
                                          'name': agent.get('name'),
                                          'connected': agent.get('connected', 'false'),
                                          'enabled': agent.get('enabled', 'false'),
                                          'authorized': agent.get('authorized', 'false'),
                                          'ip': agent.get('ip', ''), })
    print(streaming_agent_build)
    pass
