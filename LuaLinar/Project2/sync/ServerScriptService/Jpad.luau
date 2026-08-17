local JumpPad = {}
JumpPad.__index = JumpPad

function JumpPad.new(part, jumpForce)
	local jpad = {}
	setmetatable(jpad, JumpPad)
	jpad.Part = part
	jpad.JumpForce = jumpForce
	
	return jpad
end

function JumpPad:Start()
	self.Part.Touched:Connect(function(hit)
		local humanoid = hit.Parent:FindFirstChild("Humanoid")
		if humanoid then
			humanoid.JumpHeight = self.JumpForce
		end
	end)
end

return JumpPad