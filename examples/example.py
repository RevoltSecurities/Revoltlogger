from revoltlogger import Logger, LogLevel

# Basic logger instance (INFO level)
log = Logger(name="", level=LogLevel.INFO)

print("\n--- [ Basic Logging Levels ] ---\n")

log.info("This is an informational message")
log.success("Operation completed successfully!")
log.warn("This is a warning about something")
log.error("An error has occurred")
log.critical("Critical issue! Immediate attention needed.")

print("\n--- [ Advanced Logging Levels ] ---\n")

# Advanced logger (TRACE level to capture everything)
adv_log = Logger(name="AdvancedLogger", level=LogLevel.TRACE)

adv_log.trace("Tracing low-level internal flow")
adv_log.debug("Debugging variable values")
adv_log.verbose("Verbose logging for extended info")
adv_log.info("Advanced logger still shows info")
adv_log.success("Success with green highlight")
adv_log.warn("Heads up, something may be wrong")
adv_log.error("Error encountered while processing")
adv_log.critical("System failure warning")

print("\n--- [ Custom Logging ] ---\n")

# Custom level log (e.g., EXPLOIT or PAYLOAD)
adv_log.custom("EXPLOIT", "Exploit sent to target", color="\033[1;35m")  # Bright Magenta
adv_log.custom("PAYLOAD", "Payload delivered successfully", color="\033[1;36m")  # Bright Cyan
adv_log.custom("RECON", "Running passive reconnaissance phase", color="\033[1;34m")  # Bright Blue

print("\n--- [ Banner and Standard I/O Test ] ---\n")

# Display a banner
adv_log.bannerlog("🎯 Starting Subdomain Enumeration")

# Print a standard input/output message
adv_log.stdinlog("Standard output log (non-colored, stdout)")

# Change level at runtime
print("\n--- [ Dynamic Level Update ] ---\n")

log.info("Now lowering level to DEBUG")
log.level = LogLevel.DEBUG
log.debug("Now this debug message will show")

# Simulate a disabled logger
print("\n--- [ Disabled Logger Test (LogLevel.NONE) ] ---\n")

muted_log = Logger(name="SilentLogger", level=LogLevel.NONE)
muted_log.error("This will NOT be printed")
muted_log.info("Neither will this")

print("\n--- [ Done Testing revoltlogger ] ---\n")
