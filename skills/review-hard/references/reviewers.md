# Investigation methods

- **Recovery.** Start with the state that should survive a restart, rollback,
  or replay. Work backward to the commands, persisted artifacts, and
  conditions that recover that state.
- **Round Trip.** Follow a concrete value through each change in
  representation, storage and reload to the consumer. Check a supported value
  that distinguishes a correct result.
- **Remove a Step.** Fail a step while adjacent stages still work. Trace who
  reports success and what is delivered to the next consumer.
