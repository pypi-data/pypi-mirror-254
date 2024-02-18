import subprocess
import random
import string



def check_security_group_existence(security_group_name=None):
    security_group_name = str(security_group_name).strip().upper()
    cmd = f"iptables --list INPUT -n"
    output = subprocess.run(list(filter(None,cmd.split(' '))),
                   capture_output=True
                   )
    input_rules = output.stdout.decode('utf-8').split('\n')
    sg_existence = False
    for rule in input_rules:
        print(f"processing {rule}")
        if security_group_name in rule:
            sg_existence = True
            break
    return sg_existence

# check_security_group_existence('greylist')


def create_security_group(security_group_name=None,
                          table = 'filter',
                          protocol='tcp',
                          dst_port=None,
                          rule_action='append'
                          ):
    security_group_name = str(security_group_name).strip().upper()
    if not check_security_group_existence(security_group_name):
        rule_id = security_group_name + '_' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
        cmd = f"iptables -N {security_group_name}"
        # print(f"Creating Security Group: {cmd}")
        subprocess.run(list(filter(None,cmd.split(' '))))
        # cmd = f"iptables -t {table} --{rule_action} INPUT -p {protocol} --dport {dst_port} -j {security_group_name}"
        cmd = f"iptables -t {table} --{rule_action} INPUT -p {protocol} --dport {dst_port} -j {security_group_name} -m comment --comment {rule_id}"
        # print(f"Mapping Security Group: {cmd}")
        subprocess.run(list(filter(None,cmd.split(' '))))


def create_security_group_rule(table = 'filter',
                               security_group_name=None,
                               rule_action=None, # append/insert/delete
                               src_addr=None,
                               packet_action=None # drop/reject/accept
                               ):
    security_group_name = str(security_group_name).strip().upper()
    # prepare rule_id
    rule_id = security_group_name + '_' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
    # validate rule_action and packet_action
    rule_action = rule_action.strip().lower()
    packet_action = packet_action.strip().upper()
    if rule_action not in ['insert', 'append', 'delete']:
        print(f"Invalid rule action: {rule_action}")
    if packet_action not in ['DROP','REJECT','ACCEPT']:
        print(f"Invalid packet action: {packet_action}")
    cmd = f"iptables -t {table} --{rule_action} {security_group_name} -s {src_addr} -j {packet_action}"
    cmd = f"iptables -t {table} --{rule_action} {security_group_name} -s {src_addr} -j {packet_action} -m comment --comment {rule_id}"
    print(f"Executing: {cmd}")
    subprocess.run(list(filter(None,cmd.split(' '))))


def list_security_group_rules_raw(security_group_name=None):
    security_group_name = str(security_group_name).strip().upper()
    # cmd = f"iptables -L {security_group_name} -n"
    cmd = f"iptables --list-rules {security_group_name}"
    output = subprocess.run(
        list(filter(None, cmd.split(' '))),
        capture_output=True
    )
    rules = output.stdout.decode('utf-8').split('\n')
    # for rule in rules:
    #     print(rule)
    return rules
    # return rules.split('\n')


# return sg/ipaddr/action mapping
def list_security_group_rules(security_group_name=None):
    security_group_name = str(security_group_name).strip().upper()
    # cmd = f"iptables -L {security_group_name} -n"
    cmd = f"iptables --list-rules {security_group_name}"
    output = subprocess.run(
        list(filter(None, cmd.split(' '))),
        capture_output=True
    )
    rules = output.stdout.decode('utf-8').split('\n')
    rule_mapping = {}
    for rule in rules:
        if security_group_name in rule and '--comment' in rule:
            _list = rule.split()
            ipaddr = _list[3].split('/')[0]
            action = _list[-1]
            rule_mapping[ipaddr] = action
    return rule_mapping


def cleanup_security_group_rules(security_group_name=None):
    security_group_name = str(security_group_name).strip().upper()
    cmd=f"iptables -F {security_group_name}"
    subprocess.run(
        list(filter(None, cmd.split(' '))),
    )

def delete_security_group_rule(security_group_name=None, rule_id=None):
    security_group_name = str(security_group_name).strip().upper()
    existing_rules = list_security_group_rules(security_group_name)
    for rule in existing_rules:
        if rule_id in rule:
            rule_action, *fields = rule.split(' ')
            deleting_cmd = 'iptables -D ' + ' '.join(fields)
            print(f"Deleting rule: {deleting_cmd}")
            iptables_single_run(cmd=deleting_cmd)

def iptables_single_run(cmd):
    subprocess.run(
        list(filter(None, cmd.split(' '))),
    )

def delete_security_group(security_group_name=None):
    security_group_name = str(security_group_name).strip().upper()
    # step1: remove reference from INPUT
    input_rules = list_security_group_rules_raw(security_group_name='INPUT')
    for rule in input_rules:
        if security_group_name in rule:
            rule_action, *fields = rule.split(' ')
            deleting_cmd = 'iptables -D ' + ' '.join(fields)
            iptables_single_run(cmd=deleting_cmd)
    # step2: iptables -F and -X
    iptables_cmd_flush_chain = f"iptables -F {security_group_name}"
    iptables_cmd_delete_chain = f"iptables -X {security_group_name}"
    iptables_single_run(cmd=iptables_cmd_flush_chain)
    iptables_single_run(cmd=iptables_cmd_delete_chain)

def check_rule_exists():
    pass
