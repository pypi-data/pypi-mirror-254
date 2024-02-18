INSERT INTO state (title, slug) VALUES
    ('state 1', 'state_1');
INSERT INTO instrument (title, slug, host, port) VALUES
    ('instrument 1', 'instrument_1', 'host1', 9999);
INSERT INTO command (title, slug, scpi) VALUES
    ('command 1', 'command_1', 'scpi:1'),
    ('command 2', 'command_2', 'scpi:2'),
    ('command 3', 'command_3', 'scpi:3');
INSERT INTO sequence (state_id, instrument_id, command_id) VALUES
    (1, 1, 1);
