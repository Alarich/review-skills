# Finding priorities

Assign the priority after establishing the consequence. Base urgency on the supported scope, release impact and practical recovery. Keep evidence strength and fix size separate from priority.

| Priority | Meaning |
| --- | --- |
| [P0] | Stop the release or act immediately. The evidence establishes a critical release blocker such as severe data loss on a supported path with no safe recovery. Explain what blocks shipment. |
| [P1] | Fix next. A default or core workflow fails, or ordinary use risks substantial loss, a misleading release decision, or failed recovery. |
| [P2] | Fix in the normal course of work. A supported scenario yields a materially wrong result, meaningful lost work, or bounded operational failure. |
| [P3] | A smaller evidenced defect, diagnostic error, measurable or demonstrably avoidable work, or concrete maintenance friction with a specific correction. |

A broken default path is still urgent if its fix is small. A summary that disagrees with an otherwise correct detailed record can be P3 when nothing consequential depends on it. Raise priority if a shipped alert, automated action, or important operator decision uses the wrong value. Weigh a documented workaround by whether the user can still complete the supported workflow. Handle stand-alone test gaps and unresolved contract conflicts in their own report sections.
