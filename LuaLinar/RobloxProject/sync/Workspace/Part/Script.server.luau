local part = script.Parent
local startPosition = part.Position

while true do
	part.Anchored = false
	part.Transparency = 0
	part.CanCollide = true
	part.CanTouch = true
	
	wait(1.9)
	part.Position = startPosition
	part.AssemblyLinearVelocity = Vector3.zero
	part.AssemblyAngularVelocity = Vector3.zero
	
	part.Anchored = true
	part.Transparency = 1
	part.CanCollide = false
	part.CanTouch = false
	wait(2)
end
